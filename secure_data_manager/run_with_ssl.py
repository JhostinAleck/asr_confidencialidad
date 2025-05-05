import os
import sys
import ssl

from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import execute_from_command_line

# Sobrescribe el comando runserver para usar SSL
class RunServerCommand(RunserverCommand):
    def handle(self, *args, **options):
        # Configuración SSL
        os.environ['DJANGO_SETTINGS_MODULE'] = 'secure_data_manager.settings'
        
        # Ruta a certificados
        cert_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certs/cert.pem')
        key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certs/key.pem')
        
        # Verificar existencia de certificados
        if not os.path.exists(cert_path) or not os.path.exists(key_path):
            print("Error: Certificados SSL no encontrados.")
            print(f"Busqué en: {cert_path} y {key_path}")
            sys.exit(1)
        
        # Configurar SSL
        os.environ['DJANGO_HTTPS'] = 'on'
        options['ssl_certificate'] = cert_path
        options['ssl_key'] = key_path
        
        super().handle(*args, **options)

if __name__ == "__main__":
    # Reemplazar el comando runserver con nuestra versión SSL
    from django.core.management.commands.runserver import Command
    Command = RunServerCommand
    
    # Preparar argumentos
    argv = sys.argv
    if len(argv) == 1:
        argv.append('runserver')
        argv.append('0.0.0.0:8443')
    
    execute_from_command_line(argv)