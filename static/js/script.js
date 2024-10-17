document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('passwordForm');
    const passwordInput = document.getElementById('contrasena');
    const confirmPasswordInput = document.getElementById('confirmarContrasena');
    const togglePasswordButton = document.getElementById('togglePassword');
    const strengthIndicator = document.getElementById('strengthIndicator');
    const strengthText = document.getElementById('strengthText');

    // Función para actualizar la fuerza de la contraseña
    function updatePasswordStrength() {
        const password = passwordInput.value;
        let strength = 0;

        // Aumentar fuerza si cumple ciertas condiciones
        if (password.length >= 8) strength += 25;
        if (/[A-Z]/.test(password)) strength += 25;
        if (/[0-9]/.test(password)) strength += 25;
        if (/[^A-Za-z0-9]/.test(password)) strength += 25;

        // Actualizar barra de fuerza
        strengthIndicator.style.width = strength + '%';

        // Actualizar color y texto de la barra según la fuerza
        if (strength < 50) {
            strengthIndicator.style.backgroundColor = '#f56565'; // Rojo
            strengthText.textContent = 'Fuerza de la contraseña: Débil';
        } else if (strength < 75) {
            strengthIndicator.style.backgroundColor = '#ecc94b'; // Amarillo
            strengthText.textContent = 'Fuerza de la contraseña: Media';
        } else {
            strengthIndicator.style.backgroundColor = '#48bb78'; // Verde
            strengthText.textContent = 'Fuerza de la contraseña: Fuerte';
        }
    }

    // Escuchar cambios en el input de contraseña
    passwordInput.addEventListener('input', updatePasswordStrength);

    // Mostrar/Ocultar contraseña
    togglePasswordButton.addEventListener('click', function() {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        this.querySelector('i').classList.toggle('fa-eye');
        this.querySelector('i').classList.toggle('fa-eye-slash');
    });

    // Validar que las contraseñas coincidan al enviar el formulario
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (passwordInput.value === confirmPasswordInput.value) {
            console.log('Nueva contraseña establecida:', passwordInput.value);
            // Aquí puedes enviar la nueva contraseña al servidor
        } else {
            alert('Las contraseñas no coinciden.');
        }
    });
});
