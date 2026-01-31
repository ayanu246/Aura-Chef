import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AURACRAFT REPLICA", layout="wide", initial_sidebar_state="collapsed")

# --- THE ENGINE: TEXTURED VOXELS & FIRST-PERSON CAMERA ---
game_html = """
<div id="ui" style="position: absolute; top: 20px; left: 20px; z-index: 10; color: white; font-family: monospace; pointer-events: none;">
    <div>AURACRAFT V3.0 - ALPHA</div>
    <div id="stats">FPS: 60 | Blocks: 1024</div>
</div>
<div id="crosshair" style="position: absolute; top: 50%; left: 50%; width: 20px; height: 20px; border: 2px solid white; border-radius: 50%; transform: translate(-50%, -50%); z-index: 10; pointer-events: none; opacity: 0.5;">+</div>
<div id="game-container" style="width: 100%; height: 85vh; background: #000; cursor: pointer;"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    const container = document.getElementById('game-container');
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xbfd1e5); // Atmosphere Blue
    
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: false });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    // Texture Loader (Using pixelated placeholder textures for that "look")
    const loader = new THREE.TextureLoader();
    const grassTexture = loader.load('https://threejs.org/examples/textures/terrain/grasslight-big.jpg');
    grassTexture.magFilter = THREE.NearestFilter; // This makes it pixelated/blocky

    // World Logic
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshLambertMaterial({ map: grassTexture });

    // Generate Terrain (Mountains and Valleys)
    for (let x = -15; x < 15; x++) {
        for (let z = -15; z < 15; z++) {
            // Sin/Cos creates "Rolling Hills" effect
            let h = Math.floor(Math.sin(x / 4) * Math.cos(z / 4) * 3);
            
            for (let y = -2; y <= h; y++) {
                const cube = new THREE.Mesh(geometry, material);
                cube.position.set(x, y, z);
                scene.add(cube);
            }
        }
    }

    const light = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(light);
    const sun = new THREE.DirectionalLight(0xffffff, 0.5);
    sun.position.set(10, 20, 10);
    scene.add(sun);

    camera.position.set(0, 10, 20);
    camera.lookAt(0, 5, 0);

    // Click to start / Mouse Lock logic
    container.addEventListener('click', () => {
        container.requestPointerLock();
    });

    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }
    animate();
</script>
"""

# --- STREAMLIT UI ---
st.markdown("<h2 style='text-align: center; color: #34d399;'>PRIVATE REPLICA INTERFACE</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])

with col1:
    components.html(game_html, height=800)

with col2:
    st.markdown("### 🛠️ SETTINGS")
    st.selectbox("Render Distance", ["4 Chunks", "8 Chunks", "16 Chunks"])
    st.slider("Field of View (FOV)", 60, 110, 90)
    
    st.markdown("---")
    st.markdown("### 📦 INVENTORY")
    st.button("🌱 Grass Block")
    st.button("🪨 Stone Block")
    st.button("🪵 Oak Log")
    
    st.markdown("---")
    if st.checkbox("Creative Mode Fly"):
        st.write("Gravity Disabled")

st.markdown("<p style='opacity: 0.3; text-align: center;'>AURACRAFT DEV BUILD // SECURE PROTOCOL</p>", unsafe_allow_html=True)
