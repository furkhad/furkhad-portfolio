# Furkhad Ahmed — Portfolio

A dependency-free, responsive personal portfolio built with semantic HTML, modern CSS, and a small amount of vanilla JavaScript. No build step or external runtime dependencies are required for the current version.

## Run locally on Arch Linux

From this project directory:

```bash
python -m http.server 4173 --directory public
```

Open <http://127.0.0.1:4173> in Firefox. Stop the server with `Ctrl+C`.

You can also open `public/index.html` directly, but using a local HTTP server is a better test of browser behavior.

Run the dependency-free sanity check with:

```bash
python scripts/check_site.py
```

## Publish for free with Cloudflare Pages

1. Create a GitHub repository named `furkhad-portfolio`.
2. Commit and push this project to the repository.
3. In Cloudflare, open Workers & Pages and create a Pages project connected to the GitHub repository.
4. Use no build command, set the build output directory to `public`, and deploy.
5. Test the generated `*.pages.dev` URL on both desktop and phone sizes.
6. Later, buy a custom domain only if the free URL is no longer sufficient. Hosting can remain free.

See: <https://developers.cloudflare.com/pages/get-started/git-integration/>.

## OpenCode workflow

Open a terminal in the project directory and run `opencode`. First ask it to inspect the whole project without modifying anything. Then request one focused change at a time. Keep changes small and inspect the diff before committing.

Use the review prompt in `notes/OPENCODE-WORKFLOW.md` for the first pass.

## Before calling it launch-ready

Follow `notes/LAUNCH-CHECKLIST.md` for the launch process and a practical first-month plan.

- Confirm every sentence accurately describes your own work.
- Confirm you are comfortable publishing the email address shown in the Contact section. Replace it in `public/index.html` if needed.
- Review the LinkedIn and GitHub links.
- Add a real résumé PDF in `public/resume.pdf` and a clear download link once your CV is ready; no placeholder résumé is included.
- Review project READMEs, add screenshots or short demos where useful, and make sure the code is safe to publish.
- Test all links, keyboard navigation, project filtering, the mobile menu, reduced motion, and layout at small viewport widths.
- Add the final production URL to the JSON-LD `url` field and `og:url` metadata after deployment; update Open Graph metadata to absolute URLs if you choose to rely on social previews.
- Test the deployed page with Lighthouse and the W3C Nu HTML Checker.

## Important project-scoping notes

- QShield SecureAccess is described as a research/prototype simulation. Its proximity and post-quantum paths should not be described as production hardware attestation or production cryptography.
- Auto-Pentest Reporter performs active scans; only use it on systems you own or have explicit permission to assess.
- No performance numbers, CVE counts, employment history, certifications, or awards have been invented for this site.
