$(document).ready(function(){



	$("#comment-submit-button").click(function() {
		var serializedData = 
		$("#commentform").serialize();

		$.ajax({

			url: $("#commentform").data('url'),
			data: serializedData,
			type: 'post',
			success: function(response){
				$('#comment-div').append('<br><div id="comment-1" class="comment-wrap clearfix"><div class="comment-meta"><div class="comment-author vcard"><span class="comment-avatar clearfix"><img alt="" src="" class="avatar avatar-60 photo avatar-default" height="60" width="60" /></span></div></div><div class="comment-content clearfix"><div class="comment-author">'
											+ 'Me' + '<span><a href="#" title="Permalink to this comment">'
											+ 'Now' + '</a></span></div><p><br>'
											+ response.comment.body + '</p><a class="comment-reply-link" href="#"></a></div><br></div>')
			}


		})
		$('#commentform')[0].reset();


	});


});