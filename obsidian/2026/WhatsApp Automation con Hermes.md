---
tags: [proyecto, idea, whatsapp-automation, hermes]
estado: idea
relacionado: "[[Hermes Agent]]"
---

# WhatsApp Automation con Hermes

> Automatizar WhatsApp usando Hermes Agent como orquestador.

## Contexto

- Idea/necesidad identificada el viernes 01 de mayo de 2026
- Hermes puede actuar como cerebro orquestador para enviar/recibir mensajes de WhatsApp
- Posible integración con [[La AgencIA]] o proyectos de WeTech

## Opciones viables

### 1. whatsapp-web.js (recomendada)
- Librería Node.js que controla WhatsApp Web vía Puppeteer
- No requiere verificación empresarial ni API de Meta
- Hermes puede ejecutar scripts que llamen a la librería
- Se ejecuta como proceso background y Hermes lo controla

### 2. WhatsApp Business API
- Oficial de Meta, requiere número verificado como Business
- Más estable pero más burocracia

### 3. Twilio + WhatsApp Sandbox
- Sandbox gratuito para pruebas, pero mensajes con prefijo "twilio"
- Para producción requiere aprobación de Meta

## Próximos pasos

- [ ] Definir el caso de uso exacto
- [ ] Evaluar si whatsapp-web.js cubre la necesidad
- [ ] Crear skill de Hermes para la automatización
- [ ] Probar con sandbox/entorno local

---

*Creada el 02 de mayo de 2026 · Actualizada: "con Ernest" → "con Hermes"*
