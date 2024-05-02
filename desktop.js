
  // JavaScript code to check if the device is a desktop or not
  function checkDeviceType() {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
      // If the device is not a desktop, display an alert message
      alert("Please switch to a desktop device to access this page.");
    }
  }

  // Call the function when the page is loaded
  window.onload = checkDeviceType;
