 // Función para guardar la posición del scroll
 function guardarScrollPosicion() {
    sessionStorage.setItem('scrollPos', window.scrollY);
  }

  // Función para restaurar la posición del scroll
  function restaurarScrollPosicion() {
    var scrollPos = sessionStorage.getItem('scrollPos') || 0;
    window.scrollTo(0, scrollPos);
  }