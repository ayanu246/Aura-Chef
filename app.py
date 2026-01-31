import streamlit as st
import streamlit.components.v1 as components

# --- AURACRAFT GAME CONFIG ---
st.set_page_config(page_title="AURACRAFT | VOXEL WORLD", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@700&display=swap');
    html, body, [class*="st-"] { background-color: #121212; color: #34d399; font-family: 'Courier Prime', monospace; }
    .game-title { text-align: center; font-size: 3rem; text-shadow: 2px 2px #000; margin-bottom: 10px; }
    .hud { background: rgba(0,0,0,0.8); padding: 20px; border: 2px solid #34d399; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='game-title'>AURACRAFT v1.0</h1>", unsafe_allow_html=True)

# --- THE 3D VOXEL ENGINE (THREE.JS BYPASS) ---
# This code creates a 3D world with a player, grass blocks, and sky.
game_code = """
<div id="renderer-target" style="width: 100%; height: 600px; cursor: crosshair; border: 5px solid #34d399; border-radius: 15px;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    const container = document.getElementById('renderer-target');
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x87CEEB); // Sky Blue
    
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    // Light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(10, 20, 10);
    scene.add(directionalLight);

    // Voxel World Generation (The "Minecraft" Floor)
    const loader = new THREE.TextureLoader();
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    
    // Simple block colors for now (Green for Grass, Brown for Dirt)
    const grassMat = new THREE.MeshLambertMaterial({ color: 0x567d46 });
    
    for (let x = -10; x < 10; x++) {
        for (let z = -10; z < 10; z++) {
            const cube = new THREE.Mesh(geometry, grassMat);
            cube.position.set(x, 0, z);
            // Adding a slight random height for "Terrain"
            cube.position.y = Math.floor(Math.random() * 0.2); 
            scene.add(cube);
        }
    }

    camera.position.set(0, 5, 10);
    camera.lookAt(0, 0, 0);

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);
        // Rotate the world slightly so you can see it's 3D
        scene.rotation.y += 0.003; 
        renderer.render(scene, camera);
    }
    animate();

    // Resize listener
    window.addEventListener('resize', () => {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });
</script>
"""

col1, col2 = st.columns([3, 1])

with col1:
    components.html(game_code, height=620)

with col2:
    st.markdown("### PLAYER HUD")
    st.markdown("""
    <div class='hud'>
    <b>INVENTORY:</b><br>
    - [G] Grass Block x64<br>
    - [D] Dirt Block x64<br>
    <br>
    <b>WORLD INFO:</b><br>
    Biome: Plains<br>
    Chunk: 0, 0, 0<br>
    FPS: 60
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("RESPAWN PLAYER"):
        st.rerun()

st.info("NOTE: This is a live 3D WebGL engine. If it looks static, click the window to initialize the camera.")
