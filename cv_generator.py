from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import cm

output_path_final = "./YouNesta_CV.pdf"

doc = SimpleDocTemplate(output_path_final, pagesize=A4,
                        rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
styles = getSampleStyleSheet()

style_header = ParagraphStyle("header", parent=styles["Heading1"], fontSize=16, leading=20, spaceAfter=10)
style_section = ParagraphStyle("section", parent=styles["Heading2"], fontSize=13, leading=18, spaceAfter=6)
style_role = ParagraphStyle("role", parent=styles["Normal"], fontSize=11, leading=16, spaceAfter=4, leftIndent=6)
style_text = ParagraphStyle("text", parent=styles["Normal"], fontSize=10.5, leading=15, spaceAfter=10)

content = []

# Header
content.append(Paragraph("YouNesta", style_header))
content.append(Paragraph("Full-Stack specialized in Front-end / Web3", style_text))
content.append(Spacer(1, 12))

# Education
content.append(Paragraph("Education", style_section))
content.append(Paragraph("Bachelor in Project Management Web Development (Sup'internet / Epitech Digital) — 2017", style_text))
content.append(Spacer(1, 12))

# Skills
content.append(Paragraph("Skills", style_section))
content.append(Paragraph("""Front-end: ReactJS / Next.js / TypeScript / JavaScript (ES6+) / HTML / CSS / Webpack / Vite / Redux / Zustand / Styled Components / Tailwind / Storybook / Cypress / React Testing Library / Jest / Framer Motion / TanStack Table / SWR / React Query / ShadCN / i18next<br/>
Back-end: NodeJS / Express / GraphQL / REST / MongoDB / PostgreSQL / MySQL / Redis / Prisma / tRPC / WebSocket / Socket.io / JWT / OAuth2<br/>
Web3: Solana / SPL Token / Metaplex / Anchor Framework / Solana Web3.js / Jupiter API / Wagmi / Phantom SDK / Wallet Adapter / IPFS<br/>
DevOps: Docker / Jenkins / Firebase / AWS / Vercel / Netlify / Nginx / Git / GitHub / GitLab / CI/CD Pipelines / PM2 / Bash scripting<br/>
Data & Analytics: ApexCharts / Grafana / DataDog / mParticle / Google Analytics / Google AdSense / Mixpanel / BigQuery / Segment<br/>
Practices: Agile / Scrum / Kanban / Pair Programming / TDD / Code Review / Continuous Integration / Continuous Deployment / Clean Architecture / Design System Development""", style_text))
content.append(Spacer(1, 12))

# Professional Experiences
content.append(Paragraph("Professional Experiences", style_section))

experiences = [
    ("Charles.co", "February 2026 (Current)", "Senior Full-Stack Engineer – Telehealth Platform", """
Charles.co is a French telehealth platform (online medical consultations, pharmacy and patient follow-up), with Cercle, its patient coaching product. Full-stack work across the Charles monorepo (patient front-end and OMS back-office), the Cercle mobile app, Cercle Core and the onboarding. Built an MCP server on the OMS (Rails) exposing patient tools (consultations, prescriptions, orders, bills) to Intercom Fin, with JWT patient authentication, kill switch and Datadog logging. Shipped consultation and messaging features: pre-closing modal, regulatory call field, "no call needed" options, messaging page, call flow connected to the backend, feature flags. Developed the pharmacy funnel and patient space features: Body Reset program integration, Withings integration ("Ma balance" section), outro A/B test. Built doctor availability management (monthly view, saved templates, communication channels). Cercle mobile app (Expo / React Native): weekly-protocol reminders, progress charts, PostHog tracking, chat redirections per check-in, injection count in webviews, build and Android SDK maintenance. Cercle Core and onboarding: coach chat on Stream (broadcast messages, search, patient notes, check-in side effects), check-in tooling and filters, injection count question and queries, access restriction fixes (coach-scoped patient data). Refactored PostHog and Datadog integrations into an agnostic, feature-based architecture; CI, Dependabot rules, E2E refactoring, landing page updates and AI-assisted dev tooling (Cursor rules, agent skills).<br/>
<b>Tech:</b> React / React Native / Expo / TypeScript / Vite / Zustand / Tailwind / Ruby on Rails / PostgreSQL / GraphQL / Sidekiq / RSpec / MCP / Intercom Fin / Stream Chat / PostHog / Datadog
"""),
    ("Ynexis / Yakeey", "2025", "Tech Lead – Real Estate Estimation Platform", """
Ynexis develops advanced real estate estimation tools for real estate agents and professionals. Responsible for the architecture, development, and integration of AI-based estimation models. Created internal tools for model performance measurement and maintained the sales and purchase platform. Implemented a design system ensuring brand consistency across all interfaces.<br/>
<b>Tech:</b> React / Next.js / React Testing Library / Vite / ApexCharts / Rechart / MUI / Redux / TypeScript / Storybook / Cypress / Zustand / Tailwind / Jest / SWC
"""),
    ("The Fountain", "July to December 2024", "Front-end Engineer – Community Game Platform (Web3)", """
The Fountain is a Web3 tool enabling memecoin communities to create token-based games. Designed and developed the front-end architecture, integrated Solana wallets, and implemented randomized reward mechanisms connected to SPL token treasuries.<br/>
<b>Tech:</b> React / Solana / Vite / React Testing Library / Redux Toolkit / Wagmi / TanStack Query / Zustand / Phantom SDK / SPL Token JS / Tailwind / Jest
"""),
    ("Bridge USDC Cosmos ↔ Arbitrum", "2024 (Side Project)", "Full-Stack Developer – Cross-chain Bridge", """
Personal project bridging USDC across Cosmos and Arbitrum ecosystems. Designed the bridge UI, managed blockchain interactions, and handled RPC/indexer integrations for real-time validation.<br/>
<b>Tech:</b> React / TypeScript / Wagmi / Ethers.js / Vite / GraphQL / Cosmos SDK / Arbitrum SDK / Tailwind / Zustand / Jest
"""),
    ("Jupiter Perps Dashboard", "2025 (Side Project)", "Developer – Performance Tracking Tool (Solana)", """
Personal dashboard for analyzing trading performance on Jupiter Perpetuals (Solana). Built data aggregation modules and visualization dashboards for ROI and trade efficiency analysis.<br/>
<b>Tech:</b> React / Solana / Jupiter API / Vite / ApexCharts / Zustand / Tailwind / React Testing Library / Jest
"""),
    ("Top Music", "April 2023 – May 2024", "Lead React Developer", """
TopMusic is a Christian music streaming platform offering a tipping system for artists. Defined front-end architecture, built streaming interfaces, integrated tracking and payments, and led front-end delivery.<br/>
<b>Tech:</b> React / Next.js / Styled Components / Jest / React Testing Library / Redux / TypeScript / Storybook / Mangopay / Git / Vercel
"""),
    ("VEEPEE", "October 2022 – February 2023", "React Developer", """
Veepee is a European leader in private online sales. Refactored the vacation booking flow, developed new front-end components, and improved development standards in collaboration with product teams.<br/>
<b>Tech:</b> React / Next.js / Styled Components / Jest / Enzyme / React Testing Library / Redux / TypeScript / Storybook / GitLab
"""),
    ("DEEZER", "January 2022 – October 2022", "React Developer", """
Deezer is a global streaming service operating in over 180 countries. Implemented customer data platform integration, marketing standalones, and editorialized content systems.<br/>
<b>Tech:</b> React / Next.js / Styled Components / Jest / Enzyme / React Testing Library / Redux / TypeScript / Storybook / Cypress
"""),
    ("LEBONCOIN", "July 2018 – January 2022", "React Developer", """
Leboncoin is France’s largest classified ads platform. Migrated legacy booking and reservation flows to React, developed purchase options, integrated payments and delivery APIs, and produced promotional visuals.<br/>
<b>Tech:</b> React / Next.js / Styled Components / Jest / Enzyme / React Testing Library / Redux / TypeScript / Storybook / Cypress
"""),
]

for company, period, role, desc in experiences:
    content.append(Paragraph(f"<b>{company}</b> — {period}", style_role))
    content.append(Paragraph(f"<i>{role}</i>", style_role))
    content.append(Paragraph(desc, style_text))

# Languages
content.append(Spacer(1, 8))
content.append(Paragraph("Languages", style_section))
content.append(Paragraph("French: Native<br/>English: Professional", style_text))

# Build PDF
doc.build(content)
output_path_final
