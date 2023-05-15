function like(id,user_id) {
    element = document.getElementById (id);
    element.classList.add("no-box-shadow");
    element.innerText="like"
    
    const data = {'user_id':user_id,'tvshow_id':id};

    const request = new Request('http://localhost:5000//tvshow/like', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      
      // Send the request
      fetch(request)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));

    
}

function unlike(id,user_id) {
    element = document.getElementById (id);
    element.classList.add("no-box-shadow");
    element.innerText="unlike"
    
    console.log (element.innerText);
    
    const data = {'user_id':user_id,'tvshow_id':id};
    const request = new Request('http://localhost:5000//tvshow/unlike', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      
      // Send the request
      fetch(request)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
    
}