-- Tabla de Usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    usuario VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    rol ENUM('Administrador', 'Usuario') NOT NULL,
    estado ENUM('Activo', 'Inactivo') DEFAULT 'Activo',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Doctores
CREATE TABLE IF NOT EXISTS doctores (
    id_doctor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

-- Tabla de Pacientes
CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    sexo ENUM('Masculino', 'Femenino'),
    peso DECIMAL(5,2),
    altura DECIMAL(3,2),
    grupo_sanguineo ENUM('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'),
    alergias TEXT,
    enfermedades_cronicas TEXT
);

-- Tabla de Consultas
CREATE TABLE IF NOT EXISTS historial_consultas (
    id_consulta_h INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_doctor INT NOT NULL,
    diagnostico TEXT,
    tratamiento TEXT,
    observaciones TEXT,
    estado ENUM('Abierta', 'En proceso', 'Cerrada') DEFAULT 'Abierta',
    fecha_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor)
);

-- Tabla Consulta Prueba
CREATE TABLE IF NOT EXISTS consulta_prueba (
    id_consulta INT NOT NULL,
    id_prueba INT NOT NULL,
    tipo_prueba ENUM('Laboratorio', 'Post Mortem') NOT NULL,
    realizada BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_consulta) REFERENCES historial_consultas(id_consulta_h),
    FOREIGN KEY (id_prueba) REFERENCES pruebas_laboratorio(id_prueba_laboratorio),
    FOREIGN KEY (id_prueba) REFERENCES pruebas_postmortem(id_prueba_postmortem)
);

-- Tabla de Pruebas de Laboratorio
CREATE TABLE IF NOT EXISTS pruebas_laboratorio (
    id_prueba_laboratorio INT PRIMARY KEY AUTO_INCREMENT,
    id_consulta INT NOT NULL,
    nombre_prueba VARCHAR(100) NOT NULL,
    resultado TEXT,
    detalles TEXT,
    fecha_realizacion DATE,
    FOREIGN KEY (id_consulta) REFERENCES consulta_prueba(id_consulta)
);

-- Tabla de Pruebas Post Mortem
CREATE TABLE IF NOT EXISTS pruebas_postmortem (
    id_prueba_postmortem INT PRIMARY KEY AUTO_INCREMENT,
    id_consulta INT NOT NULL,
    detalles TEXT NOT NULL,
    fecha_realizacion DATE,
    FOREIGN KEY (id_consulta) REFERENCES consulta_prueba(id_consulta)
);

-- Tabla de Enfermedades
CREATE TABLE IF NOT EXISTS enfermedades (
    id_enfermedad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_enfermedad VARCHAR(100) NOT NULL,
    duracion_sintomas VARCHAR(100) NOT NULL,
    detalles TEXT
);

-- Tabla de Sintomas
CREATE TABLE IF NOT EXISTS sintomas (
    id_sintoma INT PRIMARY KEY AUTO_INCREMENT,
    nombre_sintoma VARCHAR(100) NOT NULL,
    detalles TEXT,
    intensidad ENUM('Leve', 'Moderado', 'Severo') NOT NULL,
    duracion VARCHAR(100) NOT NULL,
    frecuencia VARCHAR(100) NOT NULL,
    comentarios TEXT
);

-- Tabla de Enfermedades y Sintomas
CREATE TABLE IF NOT EXISTS enfermedades_sintomas (
    id_enfermedad INT NOT NULL,
    id_sintoma INT NOT NULL,
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedades(id_enfermedad),
    FOREIGN KEY (id_sintoma) REFERENCES sintomas(id_sintoma)
);

-- Tabla de Signos
CREATE TABLE IF NOT EXISTS signos (
    id_signo INT PRIMARY KEY AUTO_INCREMENT,
    frecuencia_cardiaca VARCHAR(50) NOT NULL,
    presion_arterial VARCHAR(50) NOT NULL,
    temperatura DECIMAL(3,2) NOT NULL,
    frecuencia_respiratoria VARCHAR(50) NOT NULL,
    spo2 VARCHAR(50) NOT NULL,
);

-- Tabla de Enfermedades y Signos
CREATE TABLE IF NOT EXISTS enfermedades_signos (
    id_enfermedad INT NOT NULL,
    id_signo INT NOT NULL,
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedades(id_enfermedad),
    FOREIGN KEY (id_signo) REFERENCES signos(id_signo)
);
