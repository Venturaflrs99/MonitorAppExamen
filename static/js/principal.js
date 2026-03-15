let contador = 5;
let intervaloId;

function actualizarDatosSistema() {
    fetch('/api/datos-sistema/')
        .then(respuesta => respuesta.json())
        .then(datos => {
            document.getElementById('cpu-porcentaje').textContent = datos.cpu.porcentaje;
            document.getElementById('cpu-nucleos').textContent = datos.cpu.nucleos;
            
            document.getElementById('ram-usado').textContent = datos.ram.usado;
            document.getElementById('ram-total').textContent = datos.ram.total;
            document.getElementById('ram-porcentaje').textContent = datos.ram.porcentaje;
            
            document.getElementById('disco-usado').textContent = datos.disco.usado;
            document.getElementById('disco-libre').textContent = datos.disco.libre;
            document.getElementById('disco-total').textContent = datos.disco.total;
            
            document.getElementById('so-nombre').textContent = datos.so.nombre;
            document.getElementById('so-version').textContent = datos.so.version;
        })
        .catch(error => console.error('Error:', error));
    
    contador = 5;
    document.getElementById('temporizador').textContent = contador;
}

function iniciarTemporizador() {
    if (intervaloId) {
        clearInterval(intervaloId);
    }
    
    intervaloId = setInterval(() => {
        contador--;
        document.getElementById('temporizador').textContent = contador;
        
        if (contador <= 0) {
            actualizarDatosSistema();
        }
    }, 1000);
}

document.addEventListener('DOMContentLoaded', () => {
    actualizarDatosSistema();
    iniciarTemporizador();
});