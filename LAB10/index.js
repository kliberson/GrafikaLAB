const scene = new THREE.Scene({ color: 0xffffff }); 
const camera = new THREE.PerspectiveCamera(100, window.innerWidth / window.innerHeight, 1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

const light = new THREE.PointLight(0xffffff, 1, 300);
light.position.set(-5, 5, 15);
camera.add(light);
scene.add(camera);

const material = new THREE.MeshPhongMaterial(
    {
        color: 0xffffff,
    }
);
const points = [
    {"x": 1.5, "y": 0},
    {"x": 1.3, "y": 0.5},
    {"x": 1.3, "y": 0.4},
    {"x": 1.1, "y": 0.7},
    {"x": 1, "y": 0.9},
    {"x": 0.6, "y": 3},
    {"x": 0.5, "y": 4},
    {"x": 1, "y": 4},
    {"x": 1, "y": 4.40},
    {"x": 0.5, "y": 4},
    {"x": 0.15, "y": 5},
];
const struct = new THREE.SphereGeometry(1.10, 35, 20);
const sphere = new THREE.Mesh(struct, material);

const geometry = new THREE.LatheGeometry(points, 32);
const lathe = new THREE.Mesh(geometry, material);
lathe.position.set(0, -4.2, 0);
scene.add(lathe);

sphere.position.set(0,1,0)
scene.add(sphere);

function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

camera.position.z = 10;

animate();