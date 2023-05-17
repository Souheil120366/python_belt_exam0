function like(id,user_id) {
    element = document.getElementById (id);
    element.classList.add("no-box-shadow");
    element.innerText="like"
    const data = {'user_id':user_id,'tvshow_id':id};
    const request = new Request('/tvshow/like', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      fetch(request)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}

function unlike(id,user_id) {
    element = document.getElementById (id);
    element.classList.add("no-box-shadow");
    element.innerText="unlike"
    const data = {'user_id':user_id,'tvshow_id':id};
    const request = new Request('/tvshow/unlike', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      fetch(request)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
    
}