var add_song = document.getElementById('modal_choose_song');
var container = document.getElementById('recommendation_container');
var song_name = document.getElementById('modal_song_name');
var user_name = document.getElementById('user_name');
var artist_name = document.getElementById('artist_name');
var rate_button = document.getElementById('rate_button');



document.addEventListener('click', function(e) {
    e = e || window.event;
    var targeta = e.target || e.srcElement,
    target = $(targeta).parent().parent().parent().parent();

    text = $(target).attr('id'); 
 
    //text = target.textContent || target.innerText;  
    if (text.length <=2 ){
      datas = recommendation[text]
      datas['user_name'] = user_name.innerHTML;
      
      $.ajax({
      url: '/test',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(datas) // converts js value to JSON string
      });
      
      
    }

    newtarget = $(targeta);
    id = $(newtarget).attr('id');
    var song_rating = document.getElementById('');
    //console.log(friend_recommendation);
}, false);







rate_button.addEventListener("click", function(e)  {
  rating_element = rate_button.previousElementSibling
  rating_value = rating_element.value
  rating_element_id = rating_element.getAttribute('id');
  console.log(rating_element_id)
  console.log(rating_element.value);
  console.log('rating above');
});




















/*

add_song.addEventListener('click', ()=> {

  alert(song_name.value);


  
  var div = document.createElement('div');
  div.classList.add('recommendation_name');
  div.innerHTML =`
  <p >${user_name.value} Recommends ${song_name.value} by ${artist_name.value}</p>
  `
  container.appendChild(div);
  //  song_name.value = "";
   // user_name.value = "";
   // artist_name.value = ""; 
 
  });

*/



//var href = document.getElementsByClassName("play")[0].parentNode.parentNode.href;
//const play_button = document.getElementById('play_button');

/*play_button.addEventListener("click", () => {
  alert(href);
});

document.getElementById("submit_button").addEventListener("click", () => {
  document.getElementById("result_container").focus();
});*/