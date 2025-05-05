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
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
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

-- Tabla de Signos
CREATE TABLE IF NOT EXISTS signos (
    id_signo INT PRIMARY KEY AUTO_INCREMENT,
    frecuencia_cardiaca VARCHAR(50) NOT NULL,
    presion_arterial VARCHAR(50) NOT NULL,
    temperatura DECIMAL(3,2) NOT NULL,
    frecuencia_respiratoria VARCHAR(50) NOT NULL,
    spo2 VARCHAR(50) NOT NULL
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
    PRIMARY KEY (id_enfermedad, id_sintoma),
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedades(id_enfermedad),
    FOREIGN KEY (id_sintoma) REFERENCES sintomas(id_sintoma)
);

-- Tabla de Enfermedades y Signos
CREATE TABLE IF NOT EXISTS enfermedades_signos (
    id_enfermedad INT NOT NULL,
    id_signo INT NOT NULL,
    PRIMARY KEY (id_enfermedad, id_signo),
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedades(id_enfermedad),
    FOREIGN KEY (id_signo) REFERENCES signos(id_signo)
);

-- Tabla de Citas
CREATE TABLE IF NOT EXISTS citas (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_doctor INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    motivo VARCHAR(255),
    estado ENUM('Pendiente', 'Confirmada', 'Cancelada', 'Reprogramada', 'Completada') DEFAULT 'Pendiente',
    observaciones TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor)
);

-- Tabla de Consultas
CREATE TABLE IF NOT EXISTS consultas (
    id_consulta INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_doctor INT NOT NULL,
    id_signo INT,
    diagnostico TEXT,
    tratamiento TEXT,
    observaciones TEXT,
    estado ENUM('Abierta', 'En proceso', 'Cerrada') DEFAULT 'Abierta',
    fecha_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor),
    FOREIGN KEY (id_signo) REFERENCES signos(id_signo)
);

-- Tabla de Pruebas de Laboratorio
CREATE TABLE IF NOT EXISTS pruebas_laboratorio (
    id_prueba_laboratorio INT PRIMARY KEY AUTO_INCREMENT,
    nombre_prueba VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla de Pruebas Post Mortem
CREATE TABLE IF NOT EXISTS pruebas_postmortem (
    id_prueba_postmortem INT PRIMARY KEY AUTO_INCREMENT,
    nombre_prueba VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla Consulta Prueba Laboratorio
CREATE TABLE IF NOT EXISTS consulta_prueba_laboratorio (
    id_consulta INT NOT NULL,
    id_prueba_laboratorio INT NOT NULL,
    resultado TEXT,
    realizada BOOLEAN DEFAULT FALSE,
    fecha_realizacion DATE,
    PRIMARY KEY (id_consulta, id_prueba_laboratorio),
    FOREIGN KEY (id_consulta) REFERENCES consultas(id_consulta),
    FOREIGN KEY (id_prueba_laboratorio) REFERENCES pruebas_laboratorio(id_prueba_laboratorio)
);

-- Tabla Consulta Prueba Post Mortem
CREATE TABLE IF NOT EXISTS consulta_prueba_postmortem (
    id_consulta INT NOT NULL,
    id_prueba_postmortem INT NOT NULL,
    detalles TEXT,
    realizada BOOLEAN DEFAULT FALSE,
    fecha_realizacion DATE,
    PRIMARY KEY (id_consulta, id_prueba_postmortem),
    FOREIGN KEY (id_consulta) REFERENCES consultas(id_consulta),
    FOREIGN KEY (id_prueba_postmortem) REFERENCES pruebas_postmortem(id_prueba_postmortem)
);

-- Tabla de Consulta Enfermedades
CREATE TABLE IF NOT EXISTS consulta_enfermedades (
    id_consulta INT NOT NULL,
    id_enfermedad INT NOT NULL,
    PRIMARY KEY (id_consulta, id_enfermedad),
    FOREIGN KEY (id_consulta) REFERENCES consultas(id_consulta),
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedades(id_enfermedad)
);

-- Tabla de Consulta Síntomas
CREATE TABLE IF NOT EXISTS consulta_sintomas (
    id_consulta INT NOT NULL,
    id_sintoma INT NOT NULL,
    PRIMARY KEY (id_consulta, id_sintoma),
    FOREIGN KEY (id_consulta) REFERENCES consultas(id_consulta),
    FOREIGN KEY (id_sintoma) REFERENCES sintomas(id_sintoma)
);

-- Vista de Historial de Pacientes
CREATE VIEW historial_paciente AS
SELECT 
    c.id_consulta,
    c.id_paciente,
    p.nombre AS nombre_paciente,
    p.apellido AS apellido_paciente,
    c.id_doctor,
    d.nombre AS nombre_doctor,
    d.especialidad,
    c.diagnostico,
    c.tratamiento,
    c.observaciones,
    c.estado,
    c.fecha_consulta
FROM consultas c
JOIN pacientes p ON c.id_paciente = p.id_paciente
JOIN doctores d ON c.id_doctor = d.id_doctor;

-- Vista de Citas Médicas
CREATE VIEW vista_citas AS
SELECT 
    c.id_cita,
    c.fecha_hora,
    c.motivo,
    c.estado,
    c.observaciones,
    c.fecha_creacion,
    p.id_paciente,
    CONCAT(p.nombre, ' ', p.apellido) AS nombre_completo_paciente,
    p.edad,
    p.sexo,
    d.id_doctor,
    d.nombre AS nombre_doctor,
    d.especialidad
FROM citas c
JOIN pacientes p ON c.id_paciente = p.id_paciente
JOIN doctores d ON c.id_doctor = d.id_doctor
ORDER BY c.fecha_hora;

-- Vista de Pruebas de Laboratorio
CREATE VIEW vista_pruebas_laboratorio AS
SELECT 
    cpl.id_consulta,
    cpl.id_prueba_laboratorio,
    pl.nombre_prueba,
    pl.descripcion,
    cpl.resultado,
    cpl.realizada,
    cpl.fecha_realizacion,
    c.id_paciente,
    CONCAT(p.nombre, ' ', p.apellido) AS nombre_paciente,
    c.id_doctor,
    d.nombre AS nombre_doctor,
    d.especialidad,
    c.fecha_consulta
FROM consulta_prueba_laboratorio cpl
JOIN pruebas_laboratorio pl ON cpl.id_prueba_laboratorio = pl.id_prueba_laboratorio
JOIN consultas c ON cpl.id_consulta = c.id_consulta
JOIN pacientes p ON c.id_paciente = p.id_paciente
JOIN doctores d ON c.id_doctor = d.id_doctor
ORDER BY cpl.fecha_realizacion DESC;

-- Vista de Pruebas Postmortem
CREATE VIEW vista_pruebas_postmortem AS
SELECT 
    cpp.id_consulta,
    cpp.id_prueba_postmortem,
    pp.nombre_prueba,
    pp.descripcion,
    cpp.detalles,
    cpp.realizada,
    cpp.fecha_realizacion,
    c.id_paciente,
    CONCAT(p.nombre, ' ', p.apellido) AS nombre_paciente,
    c.id_doctor,
    d.nombre AS nombre_doctor,
    d.especialidad,
    c.fecha_consulta
FROM consulta_prueba_postmortem cpp
JOIN pruebas_postmortem pp ON cpp.id_prueba_postmortem = pp.id_prueba_postmortem
JOIN consultas c ON cpp.id_consulta = c.id_consulta
JOIN pacientes p ON c.id_paciente = p.id_paciente
JOIN doctores d ON c.id_doctor = d.id_doctor
ORDER BY cpp.fecha_realizacion DESC;
