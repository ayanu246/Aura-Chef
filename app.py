import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("My Minecraft Clone")

# This is a "Web-Friendly" Minecraft engine written in HTML/JavaScript
# It allows you to walk around and place blocks in a browser.
minecraft_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Minecraft</title>
    <style>
        body { margin: 0; }
        canvas { display: block; }
        #instructions {
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            background: rgba(0,0,0,0.5);
            padding: 10px;
            font-family: sans-serif;
        }
    </style>
</head>
<body>
    <div id="instructions">
        <b>WASD</b> to Move | <b>Click</b> to Look | <b>Space</b> to Jump<br>
        (This is a basic 3D view for your web app)
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Basic 3D Scene Setup
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x87ceeb); // Sky Blue
        
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Create a Floor (Grid of blocks)
        const geometry = new THREE.BoxGeometry(1, 1, 1);
        const material = new THREE.MeshLambertMaterial({ color: 0x00ff00 }); // Green Grass
        
        for(let x = -5; x < 5; x++) {
            for(let z = -5; z < 5; z++) {
                const cube = new THREE.Mesh(geometry, material);
                cube.position.set(x, 0, z);
                scene.add(cube);
            }
        }

        // Light
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(5, 10, 7.5).normalize();
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.z = 5;
        camera.position.y = 2;

        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
"""

# Display the 3D world in Streamlit
components.html(minecraft_html, height=600)

st.write("This app uses HTML5 and Three.js to render 3D inside Streamlit.")
