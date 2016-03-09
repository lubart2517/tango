$(document).ready(function () {
$("#likes").click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});
$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/rango/suggest_category/', {suggestion: query}, function(data){
			$('#cats').html(data);
        });
});
$('.rango-add').click(function(){
	var catid
	catid = $(this).attr("data-catid");
	var url
	url = $(this).attr("data-url");
	var title
	title = $(this).attr("data-title");
	var me
	me = $(this)
	$.get('/rango/auto_add_page/', {category_id: catid, url: url, title: title}, function(data){
		$('#pages').html(data);
		me.hide();
	});
});
$('#id_email').keyup (function(){
        var inserted_mail;
        inserted_mail = $(this).val();
        $.get('/rango/pass_reset/', {string_mail: inserted_mail}, function(data){
        $('#mail_error').html(data);
        });
});
})