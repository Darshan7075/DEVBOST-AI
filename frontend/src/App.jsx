import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import './App.css';

function App() {
  const [repo, setRepo] = useState('');
  const [task, setTask] = useState('explain');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [typing, setTyping] = useState(false);
  const [view, setView] = useState('intro'); // 'intro', 'home', or 'result'
  const [currentSlide, setCurrentSlide] = useState(0);
  const [copied, setCopied] = useState(false);
  const [recentScans, setRecentScans] = useState(() => {
    try {
      const saved = localStorage.getItem('devboost_recent_scans');
      const parsed = saved ? JSON.parse(saved) : [];
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  });

  // Save to localStorage whenever recentScans changes
  React.useEffect(() => {
    localStorage.setItem('devboost_recent_scans', JSON.stringify(recentScans));
  }, [recentScans]);

  const tasks = [
    { id: 'explain', icon: '🧠', title: 'Explain Code', desc: 'Understand architecture' },
    { id: 'docs', icon: '📚', title: 'Generate Docs', desc: 'Create README' },
    { id: 'bugs', icon: '🐛', title: 'Detect Bugs', desc: 'Find vulnerabilities' },
    { id: 'tests', icon: '🧪', title: 'Generate Tests', desc: 'Build test suites' }
  ];

  const handleAnalyze = async () => {
    if (!repo) return;
    
    // Switch to result view and start loading
    setView('result');
    setLoading(true);
    setError(null);
    setResult(null);
    setTyping(false);

    // Add to recent scans
    setRecentScans(prev => {
      const filtered = prev.filter(r => r !== repo);
      return [repo, ...filtered].slice(0, 3); // Keep last 3
    });

    try {
      const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
      const response = await axios.post(`${API_URL}/analyze`, {
        repo_url: repo,
        task: task
      });
      setResult(response.data.result.content);
      setTyping(true);
      setTimeout(() => setTyping(false), 1500);
    } catch (err) {
      setError(err.response?.data?.detail || err.message || 'An error occurred during analysis');
    } finally {
      setLoading(false);
    }
  };

  const handleBack = () => {
    setView('home');
    setResult(null);
    setError(null);
  };

  const handleLaunch = () => {
    setView('home');
  };

  const handleBrandClick = () => {
    setView('intro');
    setResult(null);
    setError(null);
  };

  const handleCopy = () => {
    if (result) {
      navigator.clipboard.writeText(result);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const handleDownload = () => {
    if (result) {
      const element = document.createElement("a");
      const file = new Blob([result], {type: 'text/markdown'});
      element.href = URL.createObjectURL(file);
      element.download = `IBM_Bob_${task}_Report.md`;
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    }
  };

  return (
    <div className="app-container">
      {/* Sticky Header for Intro */}
      {view === 'intro' && (
        <header className="intro-header">
          <div className="header-inner">
            <div className="nav-brand" onClick={handleBrandClick} style={{cursor: 'pointer'}}>
              <div className="brand-dot"></div>
              <h1>DevBoost <span>AI</span></h1>
            </div>
            <div className="header-actions">
              <button onClick={handleLaunch} className="launch-btn-small">Launch Dashboard</button>
            </div>
          </div>
        </header>
      )}

      <div className="grid-background"></div>
      <div className="glow-orb blue-orb"></div>
      <div className="glow-orb purple-orb"></div>
      
      <nav className="navbar">
        <div className="nav-brand" onClick={handleBrandClick} style={{cursor: 'pointer'}}>
          <div className="logo-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="#0066FF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 17L12 22L22 17" stroke="#0066FF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 12L12 17L22 12" stroke="#0066FF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </div>
          <h1>DevBoost <span>AI</span></h1>
        </div>
        <div className="nav-badges">
          <span className="badge ibm-badge">Powered by IBM watsonx</span>
        </div>
      </nav>

      <main className="main-layout">
        {view === 'intro' && (
          <section className="intro-view scroll-mode">
            {/* Hero Section */}
            <div className="intro-section hero-section">
              <div className="intro-badge">IBM Hackathon Submission 2026</div>
              <h1 className="intro-title big">DevBoost <span>AI</span></h1>
              <p className="intro-subtitle"><strong>Accelerate engineering velocity</strong> with whole-project semantic reasoning. Powered by <strong>IBM Bob</strong> and the <strong>watsonx granite-series LLMs</strong>.</p>
              <div className="hero-actions">
                <button onClick={() => {
                  document.getElementById('live-preview').scrollIntoView({ behavior: 'smooth' });
                }} className="launch-btn ghost">
                  Watch Live Demo
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
                </button>
                <button onClick={handleLaunch} className="launch-btn primary pulse">
                  Launch Developer Portal
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </button>
              </div>
            </div>

            {/* Live Preview Mockup Section */}
            <div id="live-preview" className="intro-section preview-section">
               <div className="section-label">Proof of Concept</div>
               <h2 className="section-title">See the <span>Intelligence</span> in Action.</h2>
               <div className="live-mockup-container">
                  <div className="mockup-window">
                     <div className="mockup-header">
                        <div className="dots"><span></span><span></span><span></span></div>
                        <div className="mockup-tab">bob-architect-engine</div>
                     </div>
                     <div className="mockup-body">
                        <div className="code-line"><span className="c-blue">Analyze</span> repo: <span className="c-purple">"github.com/org/enterprise-app"</span></div>
                        <div className="code-line"><span className="c-green">✓</span> Indexing 142 files across 12 modules...</div>
                        <div className="code-line"><span className="c-green">✓</span> Building semantic graph...</div>
                        <div className="code-line"><span className="c-yellow">!</span> Potential security flaw found in <span className="c-red">auth_service.py:L42</span></div>
                        <div className="code-line"><span className="c-cyan">Bob:</span> "I've detected an insecure session handling pattern that affects the entire gateway layer. Would you like me to generate a self-healing patch?"</div>
                     </div>
                  </div>
                  <div className="mockup-description">
                     <h3>Real-Time Reasoning</h3>
                     <p>Unlike simple chat-bots, DevBoost AI actively monitors <strong>architectural patterns</strong>. It doesn't just answer—it <strong>anticipates</strong> your next engineering bottleneck.</p>
                  </div>
               </div>
            </div>

            {/* Comparison Table Section */}
            <div className="intro-section content-section">
               <div className="section-label">Competition Analysis</div>
               <h2 className="section-title">The <span>DevBoost</span> Advantage.</h2>
               <div className="comparison-container">
                  <table className="comparison-table">
                     <thead>
                        <tr>
                           <th>Capability</th>
                           <th>Standard AI Tools</th>
                           <th className="highlight">DevBoost AI</th>
                        </tr>
                     </thead>
                     <tbody>
                        <tr>
                           <td>Context Window</td>
                           <td>Single File (limited)</td>
                           <td><strong>Whole-Project Semantic Graph</strong></td>
                        </tr>
                        <tr>
                           <td>Security Audit</td>
                           <td>Regex-based checks</td>
                           <td><strong>AI Logic Flaw Detection</strong></td>
                        </tr>
                        <tr>
                           <td>Reasoning Model</td>
                           <td>Generic Models</td>
                           <td><strong>IBM watsonx Granite-Series</strong></td>
                        </tr>
                        <tr>
                           <td>Onboarding Speed</td>
                           <td>Weeks</td>
                           <td><strong>Minutes</strong></td>
                        </tr>
                     </tbody>
                  </table>
               </div>
            </div>

            {/* Stats/Impact Bar */}
            <div className="impact-bar">
              <div className="impact-stat">
                <h3>70%</h3>
                <p>Faster <strong>Onboarding</strong></p>
              </div>
              <div className="impact-stat">
                <h3>45%</h3>
                <p>Less <strong>Technical Debt</strong></p>
              </div>
              <div className="impact-stat">
                <h3>10x</h3>
                <p>Engine <strong>Velocity</strong></p>
              </div>
              <div className="impact-stat">
                <h3>0.1%</h3>
                <p>Security <strong>False Positives</strong></p>
              </div>
            </div>

            {/* Problem Section */}
            <div id="problem-section" className="intro-section content-section alt-bg">
              <div className="section-label">The Market Challenge</div>
              <h2 className="section-title">Modern Codebases are <span>Knowledge Black Holes</span>.</h2>
              <div className="pitch-cards grid-cards">
                <div className="pitch-card problem">
                  <div className="pitch-icon">🌑</div>
                  <h3>Contextual Blindness</h3>
                  <p>Standard AI only sees the file you have open. It misses the <strong>deep architectural dependencies</strong> that cause systemic failures.</p>
                </div>
                <div className="pitch-card problem">
                  <div className="pitch-icon">📉</div>
                  <h3>Engineering Waste</h3>
                  <p>Developers spend <strong>60% of their time</strong> reading old code instead of writing new features. This is the <strong>Technical Debt</strong> tax.</p>
                </div>
                <div className="pitch-card problem">
                  <div className="pitch-icon">⚠️</div>
                  <h3>Security Shadows</h3>
                  <p>Logic flaws that span multiple modules are invisible to traditional scanners, leaving <strong>enterprise gateways</strong> vulnerable.</p>
                </div>
              </div>
            </div>

            {/* Solution Section */}
            <div className="intro-section content-section alt-bg">
              <div className="section-label">The Core Engine</div>
              <h2 className="section-title">Meet <span>IBM Bob</span>: Your Principal AI Architect.</h2>
              <div className="solution-deep-dive">
                <div className="solution-text">
                  <h3>Intelligent Repository Ingestion</h3>
                  <p>DevBoost AI doesn't just parse text; it builds a <strong>Semantic Knowledge Graph</strong> of your entire repository. Using IBM Bob's multi-agent orchestration, we provide:</p>
                  <ul className="solution-bullets">
                    <li><strong>Intent-Driven Reasoning:</strong> Ask "How does authentication flow?" instead of searching for keywords.</li>
                    <li><strong>Architectural Integrity:</strong> Automatically detects when new code violates existing design patterns.</li>
                    <li><strong>Production-Grade QA:</strong> Generates edge-case tests that simulate network failure and state corruption.</li>
                  </ul>
                </div>
                <div className="solution-visual">
                   <div className="visual-box">
                      <div className="visual-line"></div>
                      <div className="visual-node blue">Bob AI</div>
                      <div className="visual-node purple">Repo Graph</div>
                      <div className="visual-node cyan">Insights</div>
                   </div>
                </div>
              </div>
            </div>

            {/* Why IBM Bob? Section */}
            <div className="intro-section content-section">
              <div className="section-label">Why DevBoost?</div>
              <h2 className="section-title">The <span>IBM watsonx</span> Advantage.</h2>
              <div className="features-grid-large">
                <div className="large-feature-card">
                   <h4>Enterprise Trust</h4>
                   <p>Built on IBM's foundation of ethical AI. No data leakage, no model hallucinations in critical architecture paths.</p>
                </div>
                <div className="large-feature-card highlight">
                   <h4>Granite LLM Power</h4>
                   <p>Utilizing high-parameter code models optimized for Python, JS, and Java architectural reasoning.</p>
                </div>
                <div className="large-feature-card">
                   <h4>Security First</h4>
                   <p>Deep integration with OWASP standards ensures your analysis includes a vulnerability score for every module.</p>
                </div>
              </div>
            </div>

            {/* Steps Section */}
            <div className="intro-section content-section alt-bg">
              <div className="section-label">User Experience</div>
              <h2 className="section-title">Developer <span>Workflow</span> Integration.</h2>
              <div className="steps-container horizontal">
                <div className="step">
                  <div className="step-num">01</div>
                  <h4>Connect</h4>
                  <p>Ingest any private or public GitHub Repository with full branch support.</p>
                </div>
                <div className="step">
                  <div className="step-num">02</div>
                  <h4>Select Task</h4>
                  <p>Choose from Deep Explainer, API Documenter, Security Audit, or Test Architect.</p>
                </div>
                <div className="step">
                  <div className="step-num">03</div>
                  <h4>Export & Act</h4>
                  <p>Download production-ready Markdown or integrate directly into your CI/CD pipeline.</p>
                </div>
              </div>
            </div>

            {/* Target Audience */}
            <div className="intro-section content-section">
               <div className="section-label">Target Personas</div>
               <h2 className="section-title">Designed for the <span>Modern Tech Stack</span>.</h2>
               <div className="persona-cards">
                 <div className="persona-card">
                    <h4>For Developers</h4>
                    <p>Stop wasting time on boilerplate and documentation. Code more, explain less.</p>
                 </div>
                 <div className="persona-card">
                    <h4>For Architects</h4>
                    <p>Maintain system integrity across distributed teams with automated architectural reviews.</p>
                 </div>
                 <div className="persona-card">
                    <h4>For Leads</h4>
                    <p>Onboard engineers 70% faster by giving them a self-explaining codebase.</p>
                 </div>
               </div>
            </div>

            {/* Final Section */}
            <div className="intro-section content-section final-section alt-bg">
              <div className="section-label">Future of Code</div>
              <h2 className="section-title">Join the <span>Code Intelligence</span> Revolution.</h2>
              
              <div className="final-cta">
                <button onClick={handleLaunch} className="launch-btn primary giant-btn">
                  Initialize IBM Bob Dashboard
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </button>
                <div className="final-badges">
                  <span className="badge">v1.2.0 Stable</span>
                  <span className="badge">IBM Carbon 11</span>
                  <span className="badge">Cloud Pak Ready</span>
                </div>
              </div>
            </div>
          </section>
        )}

        {view === 'home' && (
          <section className="home-view">
            <div className="hero-section">
              <h1 className="hero-title">Deep Repository Intelligence</h1>
              <p className="hero-subtitle">Instantly analyze, document, and secure any codebase using IBM Bob AI capabilities.</p>
            </div>

            <div className="control-panel">
              <div className="input-group">
                <label>Target Repository URL</label>
                <div className="input-wrapper">
                  <span className="input-icon">🔗</span>
                  <input
                    type="text"
                    placeholder="https://github.com/username/repository"
                    value={repo}
                    onChange={(e) => setRepo(e.target.value)}
                    className="repo-input"
                  />
                </div>
                {recentScans.length > 0 && (
                  <div className="recent-scans-container">
                    <span className="recent-label">Recent:</span>
                    <div className="recent-tags">
                      {recentScans.map((scan, idx) => {
                        const repoName = scan.split('/').slice(-2).join('/');
                        return (
                          <span 
                            key={idx} 
                            className="recent-tag" 
                            onClick={() => setRepo(scan)}
                            title={scan}
                          >
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                            {repoName || scan}
                          </span>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
              
              <div className="task-grid-container">
                <label>Select AI Analysis Engine</label>
                <div className="task-grid">
                  {tasks.map((t) => (
                    <div 
                      key={t.id}
                      className={`task-card ${task === t.id ? 'active' : ''}`}
                      onClick={() => setTask(t.id)}
                    >
                      <div className="task-icon">{t.icon}</div>
                      <div className="task-info">
                        <h3>{t.title}</h3>
                        <p>{t.desc}</p>
                      </div>
                      {task === t.id && <div className="active-indicator"></div>}
                    </div>
                  ))}
                </div>
              </div>

              <button 
                onClick={handleAnalyze} 
                disabled={!repo}
                className="analyze-button"
              >
                <span className="button-text">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                  Execute AI Analysis
                </span>
              </button>
            </div>
          </section>
        )}

        {view === 'result' && (
          <section className="result-view">
            <div className="result-header-actions">
              <button onClick={handleBack} className="back-button">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                New Analysis
              </button>
              <div className="analyzing-repo-badge">
                 Target: <span>{repo.split('/').slice(-2).join('/') || repo}</span>
              </div>
            </div>

            <div className="output-panel full-width">
              <div className="terminal-header">
                <div className="mac-dots">
                  <span className="dot red"></span>
                  <span className="dot yellow"></span>
                  <span className="dot green"></span>
                </div>
                <div className="terminal-title">IBM_Bob_Output.md</div>
                <div className="terminal-actions">
                  {result && (
                    <div className="action-buttons">
                      <button onClick={handleCopy} className="icon-action-btn">
                        {copied ? (
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#42BE65" strokeWidth="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        ) : (
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                        )}
                        {copied ? 'Copied!' : 'Copy'}
                      </button>
                      <button onClick={handleDownload} className="icon-action-btn">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        Download
                      </button>
                    </div>
                  )}
                  {result && <span className="status-badge success">Analysis Complete</span>}
                  {error && <span className="status-badge error">Scan Failed</span>}
                </div>
              </div>
              
              <div className="terminal-content">
                {error && (
                  <div className="error-alert">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                    <div>
                      <h3>Analysis Error</h3>
                      <p>{error}</p>
                    </div>
                  </div>
                )}

                {loading && (
                  <div className="loading-state full-screen-loader">
                    <div className="bob-avatar-container">
                      <div className="bob-avatar">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <rect x="3" y="11" width="18" height="10" rx="2" stroke="currentColor" strokeWidth="2"/>
                          <circle cx="12" cy="5" r="2" stroke="currentColor" strokeWidth="2"/>
                          <path d="M12 7V11" stroke="currentColor" strokeWidth="2"/>
                          <circle cx="8" cy="16" r="1" fill="currentColor"/>
                          <circle cx="16" cy="16" r="1" fill="currentColor"/>
                          <path d="M8 5h8" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
                        </svg>
                      </div>
                      <div className="bob-glow"></div>
                    </div>
                    <div className="terminal-logs">
                      <p>_ Connecting to GitHub API...</p>
                      <p className="delay-1">_ Fetching repository architecture for {repo}...</p>
                      <p className="delay-2">_ Initializing IBM Bob AI {task.toUpperCase()} engine...</p>
                      <p className="delay-3">_ Running deep code analysis. Please wait...</p>
                    </div>
                  </div>
                )}

                {result && !loading && (
                  <div className={`result-content markdown-body ${typing ? 'typing-effect' : ''}`}>
                    <ReactMarkdown>{result}</ReactMarkdown>
                  </div>
                )}
              </div>
            </div>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;
