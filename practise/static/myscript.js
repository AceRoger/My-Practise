
$(function(){
	console.log('IN READY')
});

$("#call").click(function(){
	console.log('Clicked')
	$.ajax({
		type : 'get',
		url : '/blog/get-data/',

		success:function(response){
			if(response.success == "true"){
				console.log("AJAX Success")
			}
		},
		error: function(response) {
            console.log(response)
        },
	});
});


//             if (response.success == "true") {
//                 $('#complaintID').text(response.complaintIdDetail.complaintID);
//                 $('#complaintType').text(response.complaintIdDetail.complaintType);
//                 $('#complaintConsumerName').text(response.complaintIdDetail.complaintConsumerName);
//                 $('#complaintConsumerNo').text(response.complaintIdDetail.complaintConsumerNo);
//                 $('#complaintStatus').text(response.complaintIdDetail.complaintStatus);
//                 $('#consumerRemark').text(response.complaintIdDetail.consumerRemark);
//                 $('#closureRemark').text(response.complaintIdDetail.closureRemark);
//                 $('#complaint_img').attr("src",response.complaintIdDetail.complaint_img);

//             }
//         },
//         error: function(response) {
//             console.log(response)

//         },
//         beforeSend: function() {
//           $("#processing").show();
//         },
//         complete: function() {
//         $("#processing").hide();
//         $('#complaint_id_modal').modal('show');
//         }
//     });
// }