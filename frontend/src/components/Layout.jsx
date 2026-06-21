import {
  NavLink,
  Outlet,
} from "react-router-dom";

const navItems = [
  { to: "/", label: "New Search", end: true },
  { to: "/jd-analysis", label: "JD Analysis" },
  { to: "/candidates", label: "Candidates" },
  { to: "/decision", label: "Decision" },
];

export default function Layout({ hasResult }) {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <NavLink className="brand" to="/">
          <span className="brand-mark">AR</span>
          <span>
            <strong>AI Recruiter</strong>
            <small>Talent intelligence</small>
          </span>
        </NavLink>

        <nav className="nav-list">
          {navItems.map((item) => {
            const disabled = (
              item.to !== "/" && !hasResult
            );

            return (
              <NavLink
                key={item.to}
                to={disabled ? "/" : item.to}
                end={item.end}
                className={({ isActive }) => (
                  [
                    "nav-link",
                    isActive ? "active" : "",
                    disabled ? "disabled" : "",
                  ]
                    .filter(Boolean)
                    .join(" ")
                )}
              >
                {item.label}
              </NavLink>
            );
          })}
        </nav>

        <div className="sidebar-footer">
          <span className="status-dot" />
          Recruiter engine ready
        </div>
      </aside>

      <main className="main-content">
        <Outlet />
      </main>
    </div>
  );
}
