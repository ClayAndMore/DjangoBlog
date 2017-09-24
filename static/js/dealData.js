$(function () {
     var date = new Date()
     var year = date.getFullYear().toString();
     life_list(year);
});

window.onload=function(){ 
     var img = document.getElementsByClassName('img-rounded');
     getNaturalWidth(img);
} 


function life_list(data) {
     var url = "/life_list/" + data + "/";
     var back = []
     $.ajax({
         type: "get",
         url: url,
         async: false,
         success: function (result,status) {
              back = result;
	     // console.log(result);
	      render_life(result);
         },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
              alert(XMLHttpRequest.status);
              alert(XMLHttpRequest.readyState);
              alert(textStatus);
          },
     })
     return back;
}

function getNaturalWidth(img) {
    for(var x=0;x<img.length;x++){	
    	var image = new Image();
    	image.src = img[x].src;
	if(image.width < image.height){
		img[x].style.width = '200px';
		img[x].style.height = '310px';
	}
    }
}



function render_life(data){
        var l=data.length;
        var toadd1 = `
          <div class="panel panel-success">
          <div class="panel-heading">
          <h3 class="panel-title">`;
        var toadd2 = `
      月</h3>
      </div>
      <div ` 
        var toadd21='class="panel-body">'
        var toadd3 ='</div>  </div>';
	var month_list = [0,0,0,0,0,0,0,0,0,0,0,0]; //存储12月是否有数据的状态
        for(var i=0;i<l;i++){
		var month = data[i]['get_month'];
		var data_img = data[i]['its_images'];
		if(month_list[month-1]){
		    var to_add = data[i]['text'];
		    to_add = '<div><br/></div>'+'['+data[i]['get_day']+'] '+to_add+'<div></div>';
		    for(var x=0;x<data_img.length;x++){
		        to_add += '<img class="img-rounded" src="' + data_img[x]['address'] + '">';
		    }
		    $("#month"+month).append(to_add);
		}
		else{	
		    var add_total = '';
		    var month_id = 'id="month'+month+'"';
		    var add_text = toadd1 + month + toadd2 + month_id + toadd21 +'['+ data[i]['get_day']+'] '+ data[i]['text'];
		    var add_day = '<div></div>';
	            var add_img = '';
		    for(var j=0;j<data_img.length;j++){
		        add_img += '<img class="img-rounded" src="'+ data_img[j]['address']+'">';
		    };
		    add_total = add_text+add_day+add_img+toadd3;
                    $("#div_header").append(add_total);
		    month_list[month-1]=1;
		}
        }
}
