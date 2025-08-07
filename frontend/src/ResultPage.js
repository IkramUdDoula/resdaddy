import React from 'react';
import { useLocation } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import './ResultPage.css';

function ResultPage() {
  const location = useLocation();
  const analysisResult = location.state?.analysisResult || 'No result found.';

  const handleDownload = () => {
    if (!analysisResult) return;
    const blob = new Blob([analysisResult], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'cv_analysis.md';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="result-container">
      <header className="result-header-main">
        <h1>CV Analysis Result</h1>
        <button onClick={handleDownload} className="download-btn-result">Download .md</button>
      </header>
      <main className="result-content">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{analysisResult}</ReactMarkdown>
      </main>
    </div>
  );
}

export default ResultPage;
