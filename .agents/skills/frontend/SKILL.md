---
name: frontend-setup
description: Instructions for setting up and managing the Next.js frontend for Student Management Pro, deployed on Vercel
---

# Frontend Section - Next.js on Vercel

## Overview
This skill covers everything related to the **Next.js** frontend, deployed on **Vercel**, for the Student Management Pro project. The frontend prioritizes **HTML/CSS** wherever possible for simplicity and control.

## Service Details
- **Framework:** Next.js (with HTML/CSS focus)
- **Hosting:** Vercel
- **Token Name:** student-management-pro (Vercel API token)
- **Location:** `frontend/` folder in project root

## Design Principles
1. **HTML/CSS First** - Use plain HTML structure and vanilla CSS for styling wherever possible
2. **Minimal JS** - Only use JavaScript/React where interactivity is needed (forms, API calls, state)
3. **Server Components** - Leverage Next.js server components for static content
4. **Responsive Design** - Mobile-first approach with CSS media queries
5. **Beautiful UI** - Modern, premium design with gradients, animations, glassmorphism

## Folder Structure
```
frontend/
├── src/
│   ├── app/
│   │   ├── layout.js            # Root layout (HTML structure)
│   │   ├── page.js              # Home/Dashboard page
│   │   ├── globals.css          # Global styles & design system
│   │   ├── students/
│   │   │   ├── page.js          # Students list page
│   │   │   └── [id]/page.js     # Student detail page
│   │   ├── courses/
│   │   │   ├── page.js          # Courses list page
│   │   │   └── [id]/page.js     # Course detail page
│   │   ├── attendance/
│   │   │   └── page.js          # Attendance page
│   │   └── grades/
│   │       └── page.js          # Grades page
│   ├── components/              # Reusable UI components
│   │   ├── Navbar.js
│   │   ├── Sidebar.js
│   │   ├── Card.js
│   │   ├── Table.js
│   │   ├── Modal.js
│   │   └── Form.js
│   └── lib/
│       ├── api.js               # API client (fetch calls to backend)
│       └── utils.js             # Helper functions
├── public/
│   ├── icons/                   # SVG icons
│   └── images/                  # Static images
├── next.config.js               # Next.js configuration
├── package.json
├── vercel.json                  # Vercel deployment config
└── README.md
```

## CSS Strategy
```css
/* Use CSS custom properties for design system */
:root {
  --primary: #6366f1;        /* Indigo */
  --secondary: #8b5cf6;      /* Violet */
  --accent: #06b6d4;         /* Cyan */
  --bg-dark: #0f172a;        /* Slate 900 */
  --bg-card: #1e293b;        /* Slate 800 */
  --text-primary: #f8fafc;   /* Slate 50 */
  --text-secondary: #94a3b8; /* Slate 400 */
  --border: #334155;         /* Slate 700 */
  --success: #10b981;
  --warning: #f59e0b;
  --error: #ef4444;
  --radius: 12px;
  --shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
}

/* Use semantic class names, not utility classes */
.card { ... }
.btn-primary { ... }
.table-container { ... }
```

## Pages (Planned)
| Page            | Route            | Description                     |
|-----------------|------------------|---------------------------------|
| Dashboard       | `/`              | Overview with stats & charts    |
| Students List   | `/students`      | Table of all students           |
| Student Detail  | `/students/[id]` | Individual student profile      |
| Courses List    | `/courses`       | Table of all courses            |
| Course Detail   | `/courses/[id]`  | Individual course info          |
| Attendance      | `/attendance`    | Mark & view attendance          |
| Grades          | `/grades`        | View & manage grades            |
| Login           | `/login`         | Authentication page             |

## Commands Reference
```bash
# Install dependencies
cd frontend && npm install

# Run development server
cd frontend && npm run dev
# Opens at http://localhost:3000

# Build for production
cd frontend && npm run build

# Deploy to Vercel
cd frontend && vercel --prod
```

## Vercel Deployment
- Connect GitHub repo to Vercel dashboard
- Set root directory to `frontend/`
- Framework preset: Next.js (auto-detected)
- Environment variables: set `NEXT_PUBLIC_API_URL` to Render backend URL

## Important Notes
- Use `fetch()` for API calls, not axios (keep dependencies minimal)
- CSS modules or global CSS preferred over CSS-in-JS
- Images should use Next.js `<Image>` component for optimization
- Use HTML semantic elements (`<nav>`, `<main>`, `<section>`, `<article>`)
- Prioritize server-side rendering for SEO and performance
