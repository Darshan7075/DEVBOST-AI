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
          <section className="intro-view">
            <div className="intro-content">
              <div className="intro-badge">Hackathon Submission</div>
              <h1 className="intro-title">DevBoost <span>AI</span></h1>
              <p className="intro-subtitle">Turn ideas into impact faster with IBM Bob.</p>
              
              <div className="pitch-cards">
                <div className="pitch-card problem">
                  <div className="pitch-icon">🚧</div>
                  <h3>The Challenge</h3>
                  <p>Developers spend countless hours trying to understand complex codebases, writing repetitive tests, and manually maintaining documentation, slowing down innovation.</p>
                </div>
                
                <div className="pitch-card solution">
                  <div className="pitch-icon">✨</div>
                  <h3>The Solution</h3>
                  <p>A smart dashboard that leverages <strong>IBM Bob</strong> to instantly analyze any GitHub repository. It reads complete context to explain logic, auto-generate docs, and build test suites in seconds.</p>
                </div>
              </div>

              <div className="intro-actions">
                <button onClick={handleLaunch} className="launch-btn">
                  Launch Dashboard
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </button>
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
