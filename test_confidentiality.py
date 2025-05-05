import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_http_connection():
    print("\n=== Prueba de Conexión HTTP (Insegura) ===")
    url = "http://34.31.143.196:8080/api/patients/"
    
    patient_data = {
        "patient_id": "P12345",
        "name": "Juan Pérez",
        "diagnosis": "Hipertensión arterial",
        "treatment": "Losartán 50mg c/12h",
        "medical_history": "Antecedentes familiares de enfermedad coronaria"
    }
    
    try:
        response = requests.post(url, json=patient_data)
        print(f"Código de estado: {response.status_code}")
        print(f"Respuesta: {response.text}")
        print("\nNota: En la captura de Wireshark, estos datos deberían ser visibles en texto plano.")
    except Exception as e:
        print(f"Error en conexión HTTP: {e}")

def test_https_connection():
    print("\n=== Prueba de Conexión HTTPS (Segura) ===")
    url = "https://34.31.143.196:443/api/patients/"
    
    patient_data = {
        "patient_id": "P67890",
        "name": "María González",
        "diagnosis": "Diabetes mellitus tipo 2",
        "treatment": "Metformina 850mg c/8h",
        "medical_history": "Obesidad, dislipidemia"
    }
    
    try:
        response = requests.post(url, json=patient_data, verify=False)
        print(f"Código de estado: {response.status_code}")
        print(f"Respuesta: {response.text}")
        print("\nNota: En la captura de Wireshark, estos datos NO deberían ser visibles en texto plano.")
    except Exception as e:
        print(f"Error en conexión HTTPS: {e}")

if __name__ == "__main__":
    print("Iniciando pruebas de confidencialidad...")
    print("IMPORTANTE: Asegúrate de tener Wireshark capturando tráfico antes de continuar.")
    input("Presiona Enter para comenzar las pruebas...")
    
    test_http_connection()
    test_https_connection()
    
    print("\nPruebas completadas. Revisa la captura de Wireshark para verificar resultados.")