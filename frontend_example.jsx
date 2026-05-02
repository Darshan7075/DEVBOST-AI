/**
 * React Component for DevBoost AI with Enhanced Prompt Levels
 * Demonstrates integration with the enhanced API
 */

import React, { useState } from 'react';

const DevBoostAnalyzer = () => {
  const [repo, setRepo] = useState('');
  const [task, setTask] = useState('explain');
  const [level, setLevel] = useState('basic');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const tasks = [
    { value: 'explain', label: 'Explain Project', description: 'Get project overview' },
    { value: 'bugs', label: 'Find Bugs', description: 'Identify bugs and security issues' },
    { value: 'docs', label: 'Generate Docs', description: 'Create documentation' },
    { value: 'tests', label: 'Generate Tests', description: 'Create test cases' }
  ];

  const levels = [
    { value: 'basic', label: 'Basic', description: 'Quick, straightforward analysis' },
    { value: 'advanced', label: 'Advanced', description: 'Structured with priorities and examples' },
    { value: 'detailed', label: 'Detailed', description: 'Comprehensive with context and links' }
  ];

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://localhost:8000/api/v1/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          repo: repo,
          task: task,
          level: level
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Analysis failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="devboost-analyzer">
      <div className="header">
        <h1>DevBoost AI - Repository Analyzer</h1>
        <p>Analyze GitHub repositories with AI-powered insights</p>
      </div>

      <div className="form-container">
        {/* Repository Input */}
        <div className="form-group">
          <label htmlFor="repo">Repository URL</label>
          <input
            id="repo"
            type="text"
            value={repo}
            onChange={(e) => setRepo(e.target.value)}
            placeholder="https://github.com/username/repository"
            className="form-control"
          />
        </div>

        {/* Task Selection */}
        <div className="form-group">
          <label htmlFor="task">Analysis Task</label>
          <select 
            id="task"
            value={task} 
            onChange={(e) => setTask(e.target.value)}
            className="form-control"
          >
            {tasks.map(t => (
              <option key={t.value} value={t.value}>
                {t.label} - {t.description}
              </option>
            ))}
          </select>
        </div>

        {/* Enhancement Level Selection */}
        <div className="form-group">
          <label htmlFor="level">Enhancement Level</label>
          <select 
            id="level"
            value={level} 
            onChange={(e) => setLevel(e.target.value)}
            className="form-control"
          >
            {levels.map(l => (
              <option key={l.value} value={l.value}>
                {l.label} - {l.description}
              </option>
            ))}
          </select>
          
          {/* Level Info */}
          <div className="level-info">
            {level === 'basic' && (
              <p className="info-text">✓ Quick analysis with straightforward output</p>
            )}
            {level === 'advanced' && (
              <p className="info-text">✓ Structured output with priorities, examples, and best practices</p>
            )}
            {level === 'detailed' && (
              <p className="info-text">✓ Comprehensive analysis with explanations and documentation links</p>
            )}
          </div>
        </div>

        {/* Analyze Button */}
        <button 
          onClick={handleAnalyze}
          disabled={!repo || loading}
          className="btn-analyze"
        >
          {loading ? 'Analyzing...' : 'Analyze Repository'}
        </button>
      </div>

      {/* Error Display */}
      {error && (
        <div className="error-container">
          <h3>Error</h3>
          <p>{error}</p>
        </div>
      )}

      {/* Results Display */}
      {result && (
        <div className="results-container">
          <div className="results-header">
            <h2>Analysis Results</h2>
            <div className="results-meta">
              <span className="badge">Status: {result.status}</span>
              <span className="badge">Task: {result.task}</span>
              <span className="badge">Level: {result.enhancement_level}</span>
            </div>
          </div>

          <div className="results-content">
            <div className="result-section">
              <h3>Repository</h3>
              <p>{result.repo}</p>
            </div>

            <div className="result-section">
              <h3>Metadata</h3>
              <ul>
                <li>Prompt Length: {result.metadata.prompt_length} characters</li>
                <li>Timestamp: {result.metadata.timestamp}</li>
              </ul>
            </div>

            <div className="result-section">
              <h3>Prompt Used</h3>
              <pre className="code-block">{result.prompt_used}</pre>
            </div>

            <div className="result-section">
              <h3>Analysis Output</h3>
              <div className="output-content">
                {result.output}
              </div>
            </div>
          </div>
        </div>
      )}

      <style jsx>{`
        .devboost-analyzer {
          max-width: 1200px;
          margin: 0 auto;
          padding: 20px;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }

        .header {
          text-align: center;
          margin-bottom: 40px;
        }

        .header h1 {
          color: #2c3e50;
          margin-bottom: 10px;
        }

        .header p {
          color: #7f8c8d;
        }

        .form-container {
          background: #f8f9fa;
          padding: 30px;
          border-radius: 8px;
          margin-bottom: 30px;
        }

        .form-group {
          margin-bottom: 20px;
        }

        .form-group label {
          display: block;
          margin-bottom: 8px;
          font-weight: 600;
          color: #2c3e50;
        }

        .form-control {
          width: 100%;
          padding: 12px;
          border: 1px solid #ddd;
          border-radius: 4px;
          font-size: 14px;
        }

        .form-control:focus {
          outline: none;
          border-color: #3498db;
        }

        .level-info {
          margin-top: 8px;
        }

        .info-text {
          color: #27ae60;
          font-size: 14px;
          margin: 0;
        }

        .btn-analyze {
          width: 100%;
          padding: 15px;
          background: #3498db;
          color: white;
          border: none;
          border-radius: 4px;
          font-size: 16px;
          font-weight: 600;
          cursor: pointer;
          transition: background 0.3s;
        }

        .btn-analyze:hover:not(:disabled) {
          background: #2980b9;
        }

        .btn-analyze:disabled {
          background: #95a5a6;
          cursor: not-allowed;
        }

        .error-container {
          background: #fee;
          border: 1px solid #fcc;
          padding: 20px;
          border-radius: 4px;
          margin-bottom: 20px;
        }

        .error-container h3 {
          color: #c0392b;
          margin-top: 0;
        }

        .results-container {
          background: white;
          border: 1px solid #ddd;
          border-radius: 8px;
          padding: 30px;
        }

        .results-header {
          border-bottom: 2px solid #3498db;
          padding-bottom: 15px;
          margin-bottom: 25px;
        }

        .results-header h2 {
          margin: 0 0 10px 0;
          color: #2c3e50;
        }

        .results-meta {
          display: flex;
          gap: 10px;
        }

        .badge {
          background: #ecf0f1;
          padding: 5px 12px;
          border-radius: 4px;
          font-size: 14px;
          color: #2c3e50;
        }

        .result-section {
          margin-bottom: 25px;
        }

        .result-section h3 {
          color: #2c3e50;
          margin-bottom: 10px;
        }

        .code-block {
          background: #2c3e50;
          color: #ecf0f1;
          padding: 15px;
          border-radius: 4px;
          overflow-x: auto;
          font-size: 13px;
          line-height: 1.5;
        }

        .output-content {
          background: #f8f9fa;
          padding: 20px;
          border-radius: 4px;
          white-space: pre-wrap;
          font-family: monospace;
        }

        ul {
          list-style: none;
          padding: 0;
        }

        ul li {
          padding: 8px 0;
          border-bottom: 1px solid #ecf0f1;
        }

        ul li:last-child {
          border-bottom: none;
        }
      `}</style>
    </div>
  );
};

export default DevBoostAnalyzer;

// Made with Bob
