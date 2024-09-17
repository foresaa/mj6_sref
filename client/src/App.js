import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [file, setFile] = useState(null);
  const [sref, setSref] = useState('');
  const [twitterId, setTwitterId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    formData.append('sref', sref);
    formData.append('twitter_id', twitterId);

    try {
      const response = await axios.post('/your-endpoint', formData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Upload</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <input
          type="text"
          placeholder="SREF"
          value={sref}
          onChange={(e) => setSref(e.target.value)}
        />
        <input
          type="text"
          placeholder="Twitter ID"
          value={twitterId}
          onChange={(e) => setTwitterId(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default App;
