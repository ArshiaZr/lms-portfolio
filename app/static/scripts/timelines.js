const url = "http://127.0.0.1:5000/api/timeline_post";

document.addEventListener("DOMContentLoaded", () => {
  const contentsDiv = document.querySelector(".timeline-contents");

  // Function to create a timeline element
  function createTimelineElement(data) {
    const timelineDiv = document.createElement("div");
    timelineDiv.classList.add("timeline");

    const timelineHeader = document.createElement("div");
    timelineHeader.classList.add("timeline-header");

    const timelineName = document.createElement("div");
    timelineName.classList.add("timeline-name");
    timelineName.textContent = data.name;

    const timelineEmail = document.createElement("div");
    timelineEmail.classList.add("timeline-email");
    timelineEmail.textContent = data.email;

    timelineHeader.appendChild(timelineName);
    timelineHeader.appendChild(timelineEmail);

    const timelineContent = document.createElement("div");
    timelineContent.classList.add("timeline-content");
    timelineContent.textContent = data.content;

    timelineDiv.appendChild(timelineHeader);
    timelineDiv.appendChild(timelineContent);

    return timelineDiv;
  }

  // Fetch data from API and render it
  async function fetchDataAndRender() {
    try {
      const response = await fetch(url);
      const data = await response.json();
      let posts = data.timeline_posts;

      if (posts) {
        posts.forEach((item) => {
          const timelineElement = createTimelineElement(item);
          contentsDiv.appendChild(timelineElement);
        });
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  const onSubmit = async (event) => {
    console.log("onSubmit");
    event.preventDefault();
    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;
    const content = document.querySelector("#content").value;

    const formData = new URLSearchParams();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("content", content);

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formData.toString(),
      });

      console.log(response);

      if (response.ok) {
        const responseData = await response.json();
        const timelineElement = createTimelineElement(responseData);
        contentsDiv.insertBefore(timelineElement, contentsDiv.firstChild);
      } else {
        console.error("Failed to post data:", response.status);
      }
    } catch (error) {
      console.error("Error posting data:", error);
    }
  };

  // Attach onSubmit event to form submission
  const form = document.querySelector("#timelineForm");
  form.addEventListener("submit", onSubmit);

  fetchDataAndRender();
});
