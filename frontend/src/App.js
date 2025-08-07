import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

function App() {
  const [cvFile, setCvFile] = useState(null);
  const [jobDesc, setJobDesc] = useState('');
  const [loading, setLoading] = useState(false);
  const [isToggled, setIsToggled] = useState(false);
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setCvFile(e.target.files[0]);
  };

  const handleJobDescChange = (e) => {
    setJobDesc(e.target.value);
  };

const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append('cv', cvFile);
      formData.append('job_desc', jobDesc);
      formData.append('use_crazy_prompt', isToggled);
      const response = await fetch(`${process.env.REACT_APP_API_URL}/analyze-cv`, {
        method: 'POST',
        body: formData,
      });
      const result = await response.json();
      if (!response.ok) {
        alert(result.error || 'Server error');
        setLoading(false);
        return;
      }
      navigate('/result', { state: { analysisResult: result.analysis } });
    } catch (err) {
      alert('Failed to process CV. Please try again.');
    }
    setLoading(false);
  };
  return (
    <div className="container">
      <header>
        <h1>ResDaddy</h1>
      </header>
      <form className="cv-form" onSubmit={handleSubmit}>
        <label className="upload-box">
          Upload CV
          <input type="file" accept=".pdf,.doc,.docx" onChange={handleFileChange} required />
        </label>
        <textarea
          placeholder="Paste Job Description here..."
          value={jobDesc}
          onChange={handleJobDescChange}
          required
        />
        <div className="toggle-container">
          <label className="toggle-switch">
            <input type="checkbox" checked={isToggled} onChange={() => setIsToggled(!isToggled)} />
            <span className="slider round"></span>
          </label>
          <span>Batshit Crazy</span>
        </div>
        <button type="submit" disabled={loading}>Submit</button>
      </form>
      {loading && <div className="loader">Processing...</div>}
      
    </div>
  );
}

export default App;
