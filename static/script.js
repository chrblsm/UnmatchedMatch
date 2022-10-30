const cursor = document.querySelector('.cursor');

        document.addEventListener('mousemove', e => {
            cursor.setAttribute("style", "top: "+(e.pageY-10)+"px; left: "+(e.pageX-10)+"px;")
        })

        document.addEventListener('click', () => {
            cursor.classList.add("expand");

            setTimeout(() => {
                cursor.classList.remove("expand");
            }, 500)
        })



$("#submitCanva").click(function() {
    query = $("#canvaQuery").val()
    alert(query);
    $.ajax({
        type:"POST",
        url:'/sendSignal',
        data: query,
        contentType: "application/json",
        dataType: 'json',
        beforeSend: function(){
            alert("COOKING");
            // $("#loader").show();
           },

       
});
  });
  
  