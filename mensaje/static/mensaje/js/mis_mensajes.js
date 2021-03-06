var seleccionarPestana = function(estado){  
  if (estado == 'pendientes'){
    // $('#li-en-espera').addClass('active');
    // $('#li-aprobadas').removeClass('active');
    // $('#li-rechazadas').removeClass('active');
    $("#contenido-pendientes").removeClass('hidden');
    $("#contenido-aprobadas").addClass('hidden');
    $("#contenido-rechazadas").addClass('hidden');
  } else if (estado == 'aprobadas'){
    // $('#li-aprobadas').addClass('active');
    // $('#li-en-espera').removeClass('active');
    // $('#li-rechazadas').removeClass('active');
    $("#contenido-aprobadas").removeClass('hidden');
    $("#contenido-pendientes").addClass('hidden');
    $("#contenido-rechazadas").addClass('hidden');
  } else if (estado == 'rechazadas'){
    // $('#li-rechazadas').addClass('active');
    // $('#li-en-espera').removeClass('active');
    // $('#li-aprobadas').removeClass('active');
    $("#contenido-rechazadas").removeClass('hidden');
    $("#contenido-aprobadas").addClass('hidden');
    $("#contenido-pendientes").addClass('hidden');
  };  
};

// Opciones de paginacion
var options = {
    currentPage: 1,
    totalPages: 10,
    size:"normal",
    alignment:"left",
    useBootstrapTooltip:true,
    numberOfPages:5,
    tooltipTitles: function (type, page, current) {
        switch (type) {
            case "first":
            return "Primera Página";
            case "prev":
            return "Anterior";
            case "next":
            return "Siguiente";
            case "last":
            return "Última Página";
            case "page":
            return "Ir a Página "+page;
        }
    },
    pageUrl: function(type, page, current){
        return "?page="+page;
    }
};

var inicializarPaginacion = function(pagActual, pagTotales, estado){
    options.currentPage = pagActual;
    options.totalPages = pagTotales;
    if ( estado == 'pendientes'){
        $('#paginacion-pendientes').bootstrapPaginator(options);        
    } else if ( estado == 'aprobadas' ){
        $('#paginacion-aprobadas').bootstrapPaginator(options);
    }
};



$(document).ready(function() {
  // Seleccionar seccion en menu de navegacion
  $(".navegacion").removeClass("active");

  $("#li-en-espera").click(function() {
    $('#li-en-espera').addClass('active');
    $('#li-aprobadas').removeClass('active');
    $("#paginacion-pendientes").removeClass('hidden');
    $("#paginacion-pendientes").addClass('active');
    $("#paginacion-aprobadas").addClass('hidden');
    $("#contenido-pendientes").removeClass('hidden');
    $("#contenido-aprobadas").addClass('hidden');
  });

  $("#li-aprobadas").click(function() {
    $('#li-aprobadas').addClass('active');
    $('#li-en-espera').removeClass('active');
    $("#paginacion-aprobadas").removeClass('hidden');
    $("#contenido-aprobadas").removeClass('hidden');
    $("#contenido-pendientes").addClass('hidden'); 
  }); 

});
