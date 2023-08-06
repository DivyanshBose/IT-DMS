function submitForm(event) {
  event.preventDefault();

  const deviceDropdown = document.getElementById("device-dropdown");
  const selectedDevice = deviceDropdown.value;
  const formData = new FormData(document.getElementById("details-form"));

  console.log("Device Type:", selectedDevice);
  for (let pair of formData.entries()) {
    console.log(pair[0] + ':', pair[1]);
  }

  alert('Component added Successfully');

        // Redirect to the viewComponent URL after successful form submission
  window.location.href = '{% url "addDevice" %}';
  
  document.getElementById("details-form").reset();

}