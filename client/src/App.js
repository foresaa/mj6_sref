import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [srefNumber, setSrefNumber] = useState("");
  const [srefDescription, setSrefDescription] = useState("");
  const [twitterId, setTwitterId] = useState("");
  const [responseMessage, setResponseMessage] = useState("");
  const [uploadedImages, setUploadedImages] = useState([]);

  // Handle file input
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !srefNumber || !srefDescription || !twitterId) {
      setResponseMessage("All fields are required");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("sref_number", srefNumber);
    formData.append("sref_description", srefDescription);
    formData.append("twitter_id", twitterId);

    try {
      const response = await axios.post(
        "https://your-backend-url/images",
        formData
      );
      setResponseMessage("File uploaded successfully!");
      console.log(response.data);
    } catch (error) {
      console.error("Error uploading file:", error);
      setResponseMessage("Failed to upload file.");
    }
  };

  // Fetch uploaded images
  const fetchImages = async () => {
    try {
      const response = await axios.get("https://your-backend-url/images");
      setUploadedImages(response.data);
    } catch (error) {
      console.error("Error fetching images:", error);
    }
  };

  // Call fetchImages when component loads
  React.useEffect(() => {
    fetchImages();
  }, []);

  return (
    <div>
      <h1>Upload Image</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <input
          type="number"
          placeholder="SREF Number"
          value={srefNumber}
          onChange={(e) => setSrefNumber(e.target.value)}
        />
        <input
          type="text"
          placeholder="SREF Description"
          value={srefDescription}
          onChange={(e) => setSrefDescription(e.target.value)}
        />
        <input
          type="text"
          placeholder="Twitter ID"
          value={twitterId}
          onChange={(e) => setTwitterId(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>

      {responseMessage && <p>{responseMessage}</p>}

      <h2>Uploaded Images</h2>
      <div>
        {uploadedImages.map((image) => (
          <div key={image.id}>
            <img
              src={`https://your-backend-url/${image.file_url}`}
              alt={image.file_name}
              width="100"
            />
            <p>{image.sref_description}</p>
            <p>{image.twitter_id}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
