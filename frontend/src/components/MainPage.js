import axios from "axios";
import React, { useState } from "react";

let MainPage = () => {
  const [data, setData] = useState();
  const onChange = (e) => {
    setData((prevState) => ({
      ...prevState,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const Upload = async () => {
      //   await fetch("http://127.0.0.1:5000/image", {
      //     method: "POST",
      //     body: formData,
      //   }).then((resp) => {
      //     resp.json().then((data) => {
      //       console.log(data);
      //     });
      //   });

      const data = await axios.post("http://127.0.0.1:5000/image", formData);
      setData(data.data.name);
    };
    console.log(data);

    Upload();
  };

  return (
    <div>
      <form
        onSubmit={handleSubmit}
        className="container mt-5 pt-5 pb-5"    
        enctype="multipart/form-data"
      >
        <div className="form-inline justify-content-center mt-5">
          <label htmlFor="image" className="ml-sm-4 font-weight-bold mr-md-4">
            Image :{" "}
          </label>
          <div className="input-group">
            <input
              type="file"
              id="image"
              name="file"
              accept="image/*"
              className="file-custom"
            />
          </div>
          <div></div>
        </div>

        <div className="input-group justify-content-center mt-4">
          <button type="submit" className="btn btn-md btn-primary">
            Upload,,,
          </button>
          <div
            type="text"
            name="data"
            id="data"
            value={data}
            onChange={onChange}
          >
            {data}
          </div>
        </div>
      </form>
    </div>
  );
};

export default MainPage;
