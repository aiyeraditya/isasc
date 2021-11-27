const firebaseConfig = {
    apiKey: "AIzaSyBSDtGDFk_6DHO5rpxpkWY3xtvy1gGRUkE",
    authDomain: "isasc-f26c0.firebaseapp.com",
    databaseURL: "https://isasc-f26c0-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "isasc-f26c0",
    storageBucket: "isasc-f26c0.appspot.com",
    messagingSenderId: "777797932718",
    appId: "1:777797932718:web:d054dbcf09b6db6070bf3f",
    measurementId: "G-WK9Z0LZCDD"
  };

  firebase.initializeApp(firebaseConfig);

  // Reference messages collection
  var messagesRef = firebase.database().ref('messages');
  
  // Listen for form submit
  document.getElementById('join-form').addEventListener('submit', submitForm);
  
  // Submit form
  function submitForm(e){
    e.preventDefault();
  
    // Get values
    var name = getInputVal('InputName');
    var email = getInputVal('InputEmail1');
    
    console.log(name);
  
    // Save message
    saveMessage(name, email);
  
    // Clear form and Redirect to Thanks page
    document.getElementById('join-form').reset();
    window.location.replace("/thanks");
  }
  
  // Function to get get form values
  function getInputVal(id){
    return document.getElementById(id).value;
  }
  
  // Save message to firebase
  function saveMessage(name, email){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
      name: name,
      email:email,
    });
  }