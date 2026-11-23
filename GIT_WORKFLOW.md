# Guía de Flujo de Trabajo Git para el Equipo — Proyecto RPG

## 1. Protección de `main` y Gobernanza [BLOCKER]

Nadie puede hacer `push` directo ni forzado a la rama `main`; todo cambio debe entrar mediante un Pull Request aprobado. Configura en GitHub (**Settings → Branches → Add branch protection rule**) la exigencia de Pull Request, mínimo 1 aprobación, y bloqueo de *force pushes* y eliminaciones. Si alguien intenta subir directo a `main`, GitHub lo rechazará automáticamente.

```bash
# Verificación de rama actual antes de trabajar (nunca debe ser main al editar)
git branch --show-current
```

## 2. Higiene del Entorno y `.gitignore` [BLOCKER]

Antes de agregar archivos, verifica siempre `git status` y nunca uses `git add .` a ciegas. El repositorio incluye un archivo `.gitignore` que bloquea carpetas locales como `__pycache__/`, `venv/` y archivos del sistema para no contaminar el historial ni provocar conflictos binarios. Si ves archivos temporales en `git status`, no los subas.

```bash
git status
# Si .gitignore ya existe, asegúrate de no forzar archivos ignorados:
git check-ignore -v __pycache__/ venv/
```

## 3. Paridad de Entorno y Dependencias (`requirements.txt`) [BLOCKER]

Todos los integrantes deben usar exactamente las mismas versiones de Python y librerías listadas en requirements.txt. Si instalas una librería nueva para tu módulo, actualiza requirements.txt y avisa al equipo de inmediato para que nadie sufra errores de importación.

**Setup inicial (una sola vez al clonar el repo):**

```bash
python -m venv venv
# Windows (PowerShell):
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```
**Si agregas una dependencia nueva:**

## Abre requirements.txt en tu editor y agrega una línea con el formato nombre-paquete>=version. No uses pip freeze ni echo. Edita el archivo a mano.

**Antes:**
pygame-ce>=2.5.8

**Después de agregar pyyaml:**
pygame-ce>=2.5.8
pyyaml>=6.0

**Incluye el cambio a requirements.txt en el mismo commit o PR donde usas la librería por primera vez.**


## 4. Propiedad de Módulos y Protocolo de Archivos Compartidos [BLOCKER]

Cada integrante edita únicamente el archivo asignado a su rol (`src/combat.py`, `src/exploration.py`, `src/ui.py`, etc.). Si tu módulo necesita modificar una clase base o constante en un archivo compartido (`src/entities.py`, `src/inventory.py`, `config.py`), avisa en el grupo antes de editarlo para evitar que dos personas cambien las mismas líneas.

```bash
# Revisa exactamente qué archivos modificaste antes de preparar tu commit
git diff --stat
```

## 5. Nomenclatura y Aislamiento de Ramas [SHOULD]

Nunca trabajes sobre `main` ni crees ramas con nombres genéricos como `test` o tu nombre personal. Crea una rama nueva desde `main` usando los prefijos `feat/` (nueva función) o `fix/` (corrección de error) seguidos del módulo correspondiente.

```bash
 # git switch -c (Git 2.23+), NO git checkout -b.
git switch main
git pull origin main
git switch -c feat/nombre-del-modulo
```

## 6. Sincronización Diaria de Ramas con `main` [BLOCKER]

Para evitar que tu rama quede desactualizada mientras otros integran cambios, descarga lo nuevo de `main` y fusiónalo dentro de tu rama al menos una vez al día y obligatoriamente antes de abrir un Pull Request. Esto reduce al mínimo los conflictos de última hora.

```bash
git switch main
git pull origin main
git switch feat/nombre-del-modulo
git merge main
# Si aparecen conflictos, sigue el protocolo del ítem 9.
```

## 7. Granularidad de Commits, Staging y Mensajes [SHOULD]

No acumules cientos de líneas de código en un solo commit al final de la semana; haz commits pequeños y frecuentes cada vez que una función o prueba funcione. Agrega cada archivo por su ruta explícita y escribe un mensaje claro con prefijo (`feat:`, `fix:`, `docs:`).

```bash
# Verifica que estás en tu rama, no en main:
git branch --show-current
git add src/tu_archivo.py
git commit -m "feat: agregar calculo de daño por turnos en combate"
# primera vez
git push -u origin feat/nombre-del-modulo
# veces siguientes
git push

```

## 8. Trabajo en Progreso y Cambio de Contexto (`git stash`) [SHOULD]

Si necesitas cambiar de rama o actualizar `main` a mitad de una tarea y tienes código sin terminar que aún no quieres guardar en un commit, usa `git stash` para guardarlo temporalmente. Nunca uses comandos destructivos como `git reset --hard` para limpiar la carpeta cuando Git te bloquee el cambio de rama.

```bash
git stash push -m "wip: avance parcial en menu de batalla"
git switch main
# Al volver a tu rama para recuperar tus cambios:
git switch feat/nombre-del-modulo
git stash pop
```

## 9. Protocolo de Resolución de Conflictos [BLOCKER]

Si al ejecutar `git merge main` o al abrir un Pull Request aparecen conflictos (`<<<<<<< HEAD`), **resuélvelos siempre dentro de tu propia rama en tu editor (VS Code)**, nunca directamente en `main` ni a ciegas en la web de GitHub. Revisa con el compañero dueño del otro bloque qué código debe conservarse, prueba que el juego corra y haz commit de la solución.

```bash
# Después de editar manualmente los archivos con conflicto en VS Code y probar el juego:
git add src/archivo_resuelto.py
git commit -m "fix: resolver conflicto de merge con main"
git push origin feat/nombre-del-modulo
```

## 10. Lista de Verificación y Prueba Rápida antes del Pull Request [BLOCKER]

Antes de abrir un Pull Request hacia `main`, asegúrate de haber sincronizado `main` en tu rama y ejecuta `python main.py` para comprobar que el juego arranca sin errores de sintaxis ni importaciones circulares. En la descripción del PR detalla qué archivo tocaste y qué probaste. El PR requiere 1 aprobación de un compañero que NO escribió el código. La descripción debe incluir: qué archivo tocaste, qué probaste, y un screenshot o log de python main.py corriendo.

```bash
python main.py
git status

# Push final. Luego abre el PR en GitHub
git push origin feat/nombre-del-modulo
```

## 11. Recuperación de Errores (`git restore` / `git revert`) [SHOULD]

Si arruinaste un archivo local antes de hacer commit, descarta solo los cambios de ese archivo con `git restore` sin tocar el resto del proyecto. Si ya hiciste `push` de un commit defectuoso a tu rama, reviértelo de forma segura creando un commit inverso con `git revert` en lugar de reescribir el historial.

```bash
# Descartar cambios locales no guardados en un solo archivo:
git restore src/tu_archivo.py

# Revertir de forma segura un commit ya subido (reemplaza <hash> por el ID del commit):
git log --oneline -n 5
git revert <hash>
git push origin feat/nombre-del-modulo
```