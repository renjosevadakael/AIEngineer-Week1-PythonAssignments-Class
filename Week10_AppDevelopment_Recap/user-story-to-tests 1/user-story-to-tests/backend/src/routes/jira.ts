import express from 'express'
import fetch from 'node-fetch'

const router = express.Router()

function extractAcceptanceCriteria(text?: string): string | undefined {
  if (!text) return undefined

  // Normalize newlines
  const normalized = text.replace(/\r\n/g, '\n')

  // 1) Look for a block-style heading like:
  //    Acceptance Criteria\n
  // or markdown-emphasized heading like: *Acceptance Criteria*\n or **Acceptance Criteria**\n
  const headingRe = /(?:^|\n)[ \t]*[*_#>-]*[ \t]*Acceptance Criteria(?:[:\s]*[*_\-\s]*)?\n/i
  const headingMatch = normalized.match(headingRe)
  if (headingMatch && typeof headingMatch.index === 'number') {
    const start = headingMatch.index + headingMatch[0].length
    const rest = normalized.slice(start)
    // End at first blank line (two consecutive newlines) or end of text
    const endMatch = rest.search(/\n\s*\n/)
    const block = endMatch >= 0 ? rest.slice(0, endMatch) : rest

    // Extract checklist items like '* [ ] item' or '- [x] item' or '1. [ ] item'
    const checklistMatches = Array.from(block.matchAll(/^[ \t]*[-*+\d\.]*[ \t]*\[[ xX]\][ \t]*(.+)$/gm))
      .map(m => m[1].trim())

    if (checklistMatches.length > 0) {
      return checklistMatches.map(line => `- ${line}`).join('\n')
    }

    // Otherwise return the trimmed block
    const trimmed = block.trim()
    if (trimmed) return trimmed
  }

  // 2) Inline form: 'Acceptance Criteria: item 1; item 2' on same line
  const inlineRe = /Acceptance Criteria[:\s\-]*([\s\S]+)/i
  const inlineMatch = normalized.match(inlineRe)
  if (inlineMatch && inlineMatch[1]) {
    const val = inlineMatch[1].trim()
    // Stop at a following newline if present
    const firstLine = val.split('\n')[0].trim()
    return firstLine || undefined
  }

  return undefined
}

// Extract acceptance criteria and return the remaining text with the criteria block removed.
function extractAcceptanceCriteriaAndRemove(text?: string): { acceptanceCriteria?: string; remaining?: string } {
  if (!text) return {}
  const normalized = text.replace(/\r\n/g, '\n')

  // Try to find block-style heading as before
  const headingRe = /(?:^|\n)[ \t]*[*_#>-]*[ \t]*Acceptance Criteria(?:[:\s]*[*_\-\s]*)?\n/i
  const headingMatch = normalized.match(headingRe)
  if (headingMatch && typeof headingMatch.index === 'number') {
    const start = headingMatch.index
    const afterHeadingIndex = headingMatch.index + headingMatch[0].length
    const rest = normalized.slice(afterHeadingIndex)
    const endMatch = rest.search(/\n\s*\n/)
    const block = endMatch >= 0 ? rest.slice(0, endMatch) : rest

    // checklist extraction
    const checklistMatches = Array.from(block.matchAll(/^[ \t]*[-*+\d\.]*[ \t]*\[[ xX]\][ \t]*(.+)$/gm)).map(m => m[1].trim())
    let criteria: string | undefined
    if (checklistMatches.length > 0) {
      criteria = checklistMatches.map(line => `- ${line}`).join('\n')
    } else {
      const trimmed = block.trim()
      if (trimmed) criteria = trimmed
    }

    // remove the heading + block (+ following blank line if present) from the normalized text
    const afterBlockIndex = afterHeadingIndex + (endMatch >= 0 ? endMatch : rest.length)
    // also remove one trailing blank line if present
    let removalEnd = afterBlockIndex
    if (normalized.slice(removalEnd).startsWith('\n')) removalEnd += 1

    const remaining = (normalized.slice(0, start) + normalized.slice(removalEnd)).replace(/\n{3,}/g, '\n\n').trim()
    return { acceptanceCriteria: criteria, remaining }
  }

  // Inline form
  const inlineRe = /Acceptance Criteria[:\s\-]*([\s\S]+)/i
  const inlineMatch = normalized.match(inlineRe)
  if (inlineMatch && inlineMatch[1]) {
    const val = inlineMatch[1].trim()
    const firstLine = val.split('\n')[0].trim()
    // remove the inline occurrence (first match) from the text
    const remaining = normalized.replace(inlineMatch[0], '').replace(/\n{3,}/g, '\n\n').trim()
    return { acceptanceCriteria: firstLine || undefined, remaining }
  }

  return {}
}

// Remove simple markdown emphasis wrappers for lines like '*User Story*' or '**Heading**'
function sanitizeDescription(text?: string): string | undefined {
  if (!text) return undefined
  let out = text.replace(/\r\n/g, '\n')

  // Replace lines that are wrapped in *...* or _..._ (1 or 2 chars) with the inner text
  out = out.replace(/^\s*([*_]{1,2})([^\n]+?)\1\s*$/gm, (_, _wrap, inner) => inner.trim())

  // Collapse more than two consecutive newlines to two
  out = out.replace(/\n{3,}/g, '\n\n')

  return out.trim()
}

router.get('/', async (req: express.Request, res: express.Response) => {
  const issueKey = String(req.query.issueKey || '')
  if (!issueKey) {
    res.status(400).json({ error: 'Missing query param: issueKey' })
    return
  }

  const JIRA_BASE_URL = process.env.JIRA_BASE_URL
  const JIRA_USER = process.env.JIRA_USER
  const JIRA_API_TOKEN = process.env.JIRA_API_TOKEN
  const JIRA_BEARER_TOKEN = process.env.JIRA_BEARER_TOKEN
  const ACCEPTANCE_FIELD = process.env.JIRA_ACCEPTANCE_FIELD // e.g. customfield_12345

  if (!JIRA_BASE_URL) {
    res.status(500).json({ error: 'JIRA_BASE_URL not configured on server' })
    return
  }

  try {
    // Build fields query: always request summary and description; optionally include acceptance custom field
    const fields = ['summary', 'description']
    if (ACCEPTANCE_FIELD) fields.push(ACCEPTANCE_FIELD)
    const jiraUrl = `${JIRA_BASE_URL.replace(/\/$/, '')}/rest/api/2/issue/${encodeURIComponent(issueKey)}?fields=${fields.join(',')}`

    const headers: Record<string, string> = {
      Accept: 'application/json'
    }

    if (JIRA_USER && JIRA_API_TOKEN) {
      const creds = Buffer.from(`${JIRA_USER}:${JIRA_API_TOKEN}`).toString('base64')
      headers['Authorization'] = `Basic ${creds}`
    } else if (JIRA_BEARER_TOKEN) {
      headers['Authorization'] = `Bearer ${JIRA_BEARER_TOKEN}`
    } else {
      res.status(500).json({ error: 'Jira credentials not configured on server' })
      return
    }

    const r = await fetch(jiraUrl, { headers })
    if (!r.ok) {
      const txt = await r.text().catch(() => '')
      res.status(r.status).json({ error: txt || `Jira responded with ${r.status}` })
      return
    }

    const json: any = await r.json()

    const title = json?.fields?.summary
    const rawDescription = json?.fields?.description
    // First try to get acceptance criteria from a configured custom field
    let acceptanceCriteria: string | undefined
    if (ACCEPTANCE_FIELD && json?.fields && Object.prototype.hasOwnProperty.call(json.fields, ACCEPTANCE_FIELD)) {
      acceptanceCriteria = json.fields[ACCEPTANCE_FIELD]
    }

    // Extract and remove acceptance criteria block from the description so the returned description doesn't include it
    const { acceptanceCriteria: extracted, remaining } = extractAcceptanceCriteriaAndRemove(rawDescription)
    if (!acceptanceCriteria && extracted) acceptanceCriteria = extracted

    const description = sanitizeDescription(remaining ?? rawDescription)

    res.json({ title, description, acceptanceCriteria })
  } catch (err) {
    console.error('Error fetching Jira issue:', err)
    res.status(500).json({ error: 'Failed to fetch Jira issue' })
  }
})

export default router
