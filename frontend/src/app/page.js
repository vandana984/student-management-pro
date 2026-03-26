import './globals.css';

export default function Home() {
  return (
    <main className="main">
      <nav className="nav">
        <div className="logo">
          STUDENT<span>MANAGEMENT</span>PRO
        </div>
        <div className="nav-links">
          <a href="/login" className="btn btn-secondary" style={{ padding: '0.5rem 1.5rem', fontSize: '0.875rem' }}>LOG IN</a>
        </div>
      </nav>

      <section className="hero">
        <h1>
          Empowering the Next Generation 
          <span>of Academic Excellence.</span>
        </h1>
        <p>
          A unified, high-performance platform for managing students, courses, 
          grading, and attendance with seamless efficiency.
        </p>
        <div className="cta-group">
          <a href="/signup" className="btn btn-primary">
            GET STARTED 
            <span style={{ marginLeft: '10px' }}>&rarr;</span>
          </a>
          <a href="/demo" className="btn btn-secondary">
            EXPLORE PLATFORM
          </a>
        </div>
      </section>

      <div className="stats">
        <div className="stat-item">
          <h3>2.5k+</h3>
          <p>Active Students</p>
        </div>
        <div className="stat-item">
          <h3>150+</h3>
          <p>Course Modules</p>
        </div>
        <div className="stat-item">
          <h3>99.9%</h3>
          <p>Platform Uptime</p>
        </div>
      </div>
      
      <footer style={{ marginTop: 'auto', padding: '4rem 0 2rem', color: 'var(--text-dim)', fontSize: '0.875rem', width: '100%', textAlign: 'center' }}>
        &copy; 2026 Student Management Pro. Built with Next.js & FastAPI.
      </footer>
    </main>
  );
}
