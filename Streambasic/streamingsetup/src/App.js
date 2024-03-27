import './App.css';
import React, { useState, useRef } from 'react';

function VideoCapture() {
    const [stream, setStream] = useState(null);
    const videoRef = useRef();

    // Function to start video capture
    const startCapture = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            setStream(stream);
            if (videoRef.current) {
                videoRef.current.srcObject = stream;
            }
        } catch (err) {
            console.error('Error accessing webcam:', err);
        }
    };

    // Function to stop video capture
    const stopCapture = () => {
        if (stream) {
            const tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
            setStream(null);
        }
    };

    return (
        <div>
            <h1>Video Capture</h1>
            <video ref={videoRef} width="400" height="300" autoPlay></video>
            <button onClick={startCapture}>Start Capture</button>
            <button onClick={stopCapture}>Stop Capture</button>
        </div>
    );
}

export default VideoCapture;
