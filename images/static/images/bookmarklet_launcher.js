(function(){
	alert('toto')
	if(window.myBookmarklet != undefined){
		
		myBookmarklet()
	}
	else{
		script = document.createElement('script');
		source = 'http://127.0.0.1:8000/static/images/bookmarklet.js?r=';
		random_int = Math.floor(Math.random() * 1000000000000000);
		script.src = source+random_int;
	}
})();