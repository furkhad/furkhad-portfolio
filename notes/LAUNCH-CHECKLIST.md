# Launch and reach checklist

## Before publishing

- Read every project description and confirm it matches what the code currently does.
- Confirm the email address and LinkedIn URL you want to show publicly.
- Review all repositories for secrets, tokens, private logs, sensitive screenshots, and unlicensed third-party assets.
- Add a real `public/resume.pdf` and a download link when the CV is final. Do not publish a placeholder CV.
- Improve each featured repository README so it explains the problem, architecture, install/run steps, safe-use limits, screenshots, and known limitations.
- Pin the three strongest repositories on GitHub and add useful repository descriptions/topics.
- Run `python scripts/check_site.py` and test the site locally in Firefox at desktop and mobile widths.

## Publish

1. Create a GitHub repository for the portfolio, commit the reviewed source, and push `main`.
2. Import that repository into Cloudflare Pages. Framework preset: none. Build command: leave blank. Build output directory: `public`.
3. Wait for the deployment status to report success, then open the live URL in a private browser window and on a phone.
4. Test all navigation, project filters, email/contact links, external repositories, résumé download (if present), and social-preview metadata.
5. Replace the temporary relative Open Graph image URL with the absolute production URL. Add the production URL to the JSON-LD Person object, add `og:url` and canonical metadata, and create a sitemap with the real site URL.
6. Push those metadata changes and verify the new production deployment.
7. Use Google's Rich Results Test / Search Console for indexing and check the page with PageSpeed Insights. Passing tools does not guarantee search ranking.

## First 30 days after launch

### Week 1: make the evidence stronger

- Add one authentic screenshot or short demo clip to each of the three strongest projects.
- Write a short technical case study for QShield, StreamSentinel, and Auto-Pentest Reporter. Explain the problem, architecture, decisions, what you personally implemented, how you tested it, and current limitations.
- Do not publish unsupported performance numbers. Measure results before reporting them.

### Week 2: make repositories easier to review

- Pin and tidy the repositories featured on the site.
- Re-run installation steps from a clean environment and document anything a reviewer might otherwise get stuck on.
- Add safe, reproducible tests. For Auto-Pentest Reporter, make the authorization warning visible and use only approved targets in examples.

### Week 3: start sharing technical work

- Publish one LinkedIn post with the problem, a screenshot/demo, one engineering decision, one limitation, and the repository link.
- Ask for specific feedback from people working in SOC, detection engineering, and cybersecurity rather than posting only “check out my portfolio.”
- Reach out to a small number of relevant alumni, engineers, and recruiters with a tailored note and one relevant project.

### Week 4: improve based on evidence

- Review site visits or recruiter feedback if analytics are available without adding unnecessary tracking.
- Fix unclear project descriptions, broken setup instructions, or confusing navigation before adding more effects.
- Apply consistently to relevant roles. The portfolio supports outreach and applications; it does not replace them.

## Standards for project write-ups

For each significant project, be able to answer:

1. What problem does it solve, and for whom?
2. What did I personally implement?
3. What is the architecture and why were those technologies chosen?
4. How can another person reproduce the result?
5. What evidence shows that it works?
6. What are its limitations, failure modes, and next steps?
