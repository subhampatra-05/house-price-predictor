document.getElementById("predictForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const area = parseFloat(document.getElementById("area").value);
  const bedrooms = parseInt(document.getElementById("bedrooms").value);
  const bathrooms = parseInt(document.getElementById("bathrooms").value);

  if (area < 300 || bedrooms <= 0 || bathrooms <= 0) {
    document.getElementById("result").innerText = "❌ Please enter valid values.";
    return;
  }

  const data = {
    area: area,
    bedrooms: bedrooms,
    bathrooms: bathrooms
  };

  document.getElementById("result").innerText = "⏳ Predicting...";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    if (result.predicted_price) {
      document.getElementById("result").innerText = result.predicted_price;
    } else {
      document.getElementById("result").innerText = "❌ Error: " + (result.error || "Unknown error");
    }

  } catch (error) {
    console.error(error);
    document.getElementById("result").innerText = "❌ Server error. Try again later.";
  }
});