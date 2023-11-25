************************
Applications
************************

Deeper knowledge in these area will aid in understanding applications of FPGAs.
Remember.. FPGAs are just a means to an end.

Because it is versatile, it is also a cross-section of many different engineering subjects/topics.
NOTE ONLY COVER THAT WHICH YOU'VE DONE. 
other areas will be brief.



Digital Systems
##########################
The world is analog. We need a means to go to and fro.

    DAC

    ADC

Computer Architecture
##########################

Signals and System
##########################

DSP (Digital Signal Processing)
******************************************
FPGAs are often used for implementing DSP algorithms such as filtering, modulation, and demodulation. Their parallel processing capabilities make them well-suited for real-time signal processing tasks.

FPGA-based Digital Signal Processing (DSP) involves using the configurable logic and dedicated DSP resources within an FPGA to implement signal processing algorithms. FPGAs are well-suited for DSP applications due to their parallel processing capabilities, reconfigurability, and ability to efficiently implement complex algorithms. Here's an overview of the steps involved in implementing DSP in an FPGA:

Select an FPGA with DSP Blocks:

Choose an FPGA that includes dedicated DSP blocks or slices. These DSP blocks typically consist of dedicated multiplier-accumulator (MAC) units, adders, and other specialized resources optimized for signal processing tasks.
Understand DSP Algorithms:

Familiarize yourself with the DSP algorithms required for your application. DSP encompasses a wide range of algorithms, including filtering, convolution, Fourier transforms, modulation, and more. Choose algorithms that match the processing requirements of your application.
Use High-Level Synthesis (HLS):

Consider using High-Level Synthesis (HLS) tools provided by FPGA vendors. HLS allows you to describe DSP algorithms using higher-level languages such as C or MATLAB, and automatically generate the corresponding hardware description (HDL) code for the FPGA.
Parallel Processing:

Leverage the parallel processing capabilities of FPGAs for efficient implementation of DSP algorithms. Use parallelism to process multiple data samples simultaneously, taking advantage of the parallel resources available in the FPGA.
Optimize for Pipelining:

Utilize pipelining to maximize throughput. Pipelining involves breaking down the DSP algorithm into stages and processing multiple data samples concurrently. This helps reduce latency and increase the overall processing speed.
Implement Custom Accelerators:

For computationally intensive DSP tasks, design custom hardware accelerators using the dedicated DSP resources on the FPGA. This may involve optimizing algorithms for fixed-point arithmetic, exploiting parallelism, and designing efficient architectures.
Filter Design:

Implement digital filters for applications such as low-pass, high-pass, band-pass, or adaptive filters. Use FPGA resources to efficiently implement filter structures like Finite Impulse Response (FIR) or Infinite Impulse Response (IIR) filters.
FFT and DFT Implementations:

Implement Fast Fourier Transform (FFT) or Discrete Fourier Transform (DFT) algorithms for frequency domain analysis. FPGAs can efficiently parallelize and accelerate FFT computations.
Signal Modulation and Demodulation:

Implement modulation and demodulation algorithms for applications such as wireless communication or software-defined radio. FPGA-based DSP allows for real-time processing of modulated signals.
Control Systems and PID Controllers:

Implement control systems and Proportional-Integral-Derivative (PID) controllers for applications involving feedback control. FPGA-based DSP is well-suited for real-time control applications.
Simulations and Verification:

Use simulation tools to verify the functionality and performance of your DSP algorithms before implementation on the FPGA. Simulations help catch errors and optimize the design.
Interface with External Components:

Interface the FPGA-based DSP system with external components, such as sensors, actuators, or other devices, to complete the overall system.
Real-Time Processing:

Optimize your DSP design for real-time processing, taking advantage of the low-latency capabilities of FPGAs. This is particularly important for applications that require immediate responses.
Documentation and Testing:

Document your DSP design thoroughly, including signal flow diagrams, block diagrams, and parameter settings. Perform extensive testing to validate the correctness and performance of the FPGA-based DSP system.
Power Considerations:

Consider power consumption, especially for applications where power efficiency is crucial. Optimize your design for power consumption while meeting performance requirements.
When working on FPGA-based DSP, it's important to leverage the documentation and tools provided by the FPGA vendor, understand the specifics of the DSP algorithms you are implementing, and thoroughly test your design to ensure it meets the desired performance criteria.


Filter
========================================

Digital filtering is a process used in signal processing to manipulate digital signals by modifying their frequency content or other characteristics. It involves the application of digital filter algorithms to achieve specific filtering objectives. Digital filters are crucial in various applications, such as audio processing, image processing, telecommunications, and control systems.

There are two main types of digital filters:

Finite Impulse Response (FIR) Filters:

Characteristics: FIR filters have a finite impulse response, meaning that their output is solely determined by the weighted sum of the current and past input samples.
Design: FIR filters are often designed using methods like windowing, frequency sampling, or optimal methods.
Advantages: They provide linear phase response, simplicity in design, and stability.
Infinite Impulse Response (IIR) Filters:

Characteristics: IIR filters have an infinite impulse response, meaning that their output depends on both current and past input samples as well as past output samples.
Design: IIR filters are designed using techniques like Butterworth, Chebyshev, or elliptic filter design methods.
Advantages: They can achieve a desired frequency response with fewer coefficients than FIR filters but may introduce phase distortion.
Common Digital Filter Applications:

Low-pass, High-pass, Band-pass, and Band-stop Filtering:

Used to pass or reject certain frequency components of a signal.
Smoothing and Noise Reduction:

FIR and IIR filters are used to smooth signals and reduce noise in applications such as sensor data processing.
Equalization:

Adjusting the frequency response of a signal to compensate for variations in the system.
Digital Audio Processing:

Filters are applied for tasks like equalization, echo cancellation, and noise reduction in audio signals.
Image Processing:

Filters are used to enhance or blur images, reduce noise, and perform other operations.
Filter Implementation:

Filters can be implemented in software (e.g., using programming languages like Python or MATLAB) or in hardware (e.g., using digital signal processors or FPGA). The implementation method depends on factors such as the required processing speed, available resources, and the complexity of the filtering algorithm.

Overall, digital filtering is a powerful tool in signal processing, enabling the manipulation and enhancement of digital signals in a wide range of applications.



Advanced digital filters go beyond basic finite impulse response (FIR) and infinite impulse response (IIR) filters, offering more sophisticated techniques for signal processing. Some advanced digital filters and techniques include:

Adaptive Filters:

Overview: These filters adjust their characteristics in real-time based on the input signal, making them suitable for applications with changing environments or unknown system parameters.
Applications: Adaptive filters are used in fields like communications, audio processing, and biomedical signal processing.
Kalman Filters:

Overview: Widely used in control systems and estimation problems, Kalman filters combine information from sensors with a system model to estimate the state of a dynamic system.
Applications: Navigation systems, tracking systems, and robotics often employ Kalman filters for state estimation.
Wavelet Filters:

Overview: Wavelet filters decompose signals into different frequency components at different resolutions. They are well-suited for both time and frequency domain analysis.
Applications: Image compression, denoising, and signal compression benefit from wavelet filters.
Multirate Filters:

Overview: Multirate filters involve changing the sample rate of a signal to process it more efficiently. Decimation (downsampling) and interpolation (upsampling) are common techniques.
Applications: Digital audio processing, software-defined radios, and efficient spectrum analysis.
Fractional Delay Filters:

Overview: These filters allow for the introduction of fractional delays in a signal, providing precise time-domain control.
Applications: Audio processing, where fractional delays are crucial for achieving certain effects.
Fractional Order Filters:

Overview: These filters use fractional order differential or integration operators in their design, allowing for more flexible frequency response shaping.
Applications: Biomedical signal processing, communication systems, and control systems.
Savitzky-Golay Filters:

Overview: These filters combine smoothing and differentiation, making them suitable for preserving features in signals while reducing noise.
Applications: Analyzing chromatographic and spectroscopic data in chemistry, and processing noisy sensor data.
Comb Filters:

Overview: Comb filters are used to remove or enhance periodic components in a signal.
Applications: Eliminating interference or echo in communication systems.
Hilbert Transform Filters:

Overview: These filters introduce a 90-degree phase shift, making them useful for analyzing the instantaneous frequency and phase of a signal.
Applications: Signal processing in communications, radar, and audio analysis.
These advanced filters provide more specialized and often more efficient solutions for specific signal processing tasks. The choice of a filter depends on the particular requirements and characteristics of the application at hand.






Modulation
========================================
FPGA-based modulation involves using a Field-Programmable Gate Array (FPGA) to implement digital modulation schemes for communication systems. Digital modulation is a process where digital data is encoded into analog signals for transmission over a communication channel. FPGA devices offer flexibility and programmability, making them suitable for implementing various modulation techniques. Here are some key points on FPGA-based modulation:

Modulation Schemes:

FPGA can be used to implement various modulation schemes, including:
Binary Phase Shift Keying (BPSK): Modulates data using phase shifts of 0 and 180 degrees.
Quadrature Phase Shift Keying (QPSK): Uses four phase shifts for increased data rate.
Quadrature Amplitude Modulation (QAM): Combines amplitude and phase shifts for higher data rates.
Digital Signal Processing (DSP):

FPGA devices often include DSP blocks that can be used to efficiently implement complex modulation and demodulation algorithms. These blocks enable parallel processing, improving performance.
Parallelism and Pipelining:

Exploit the parallel processing capabilities of FPGAs to implement parallel architectures for modulation. Pipelining can be used to improve throughput and reduce latency.
FPGA Resources:

Consider the resources available on the FPGA, such as lookup tables (LUTs), flip-flops, and DSP blocks. Efficient utilization of these resources is crucial for achieving optimal performance.
Modulation Core Implementation:

Design and implement the modulation core using a hardware description language (HDL) such as VHDL or Verilog. The core should handle the generation of modulated signals based on the input data.
Integration with Communication Systems:

Integrate the FPGA-based modulation core into the broader communication system. This involves interfacing with other components such as data sources, channel encoding, and RF components.
Real-Time Processing:

FPGAs are capable of real-time processing, making them suitable for applications that require low-latency modulation. Real-time capabilities are crucial in communication systems where timely signal processing is essential.
Software-Defined Radio (SDR):

FPGAs are commonly used in Software-Defined Radio applications where modulation schemes can be reconfigured in real-time. This flexibility allows for adapting to different communication standards.
Simulation and Verification:

Simulate the FPGA design using tools such as ModelSim or VCS to verify the functionality and performance of the modulation core before deployment.
FPGA Development Tools:

Use the development tools provided by FPGA vendors to facilitate design, synthesis, and implementation. These tools often include IP cores and libraries for signal processing.
Clock and Timing Considerations:

Pay attention to clock domains and timing constraints to ensure proper synchronization in the modulation process.
Implementing modulation on an FPGA involves a balance between algorithm complexity, resource utilization, and performance requirements. Careful design and optimization are necessary to meet the specific needs of the communication system.

Demodulating
========================================
FPGA-based demodulation involves the use of a Field-Programmable Gate Array (FPGA) to implement digital signal processing algorithms that extract information from a modulated signal. The demodulation process depends on the modulation scheme used in the communication system. Here are general steps and considerations for FPGA-based demodulation:

Choose Modulation Scheme:

Identify the modulation scheme used in the communication system. Common modulation schemes include Binary Phase Shift Keying (BPSK), Quadrature Phase Shift Keying (QPSK), and Quadrature Amplitude Modulation (QAM).
Signal Acquisition:

Implement signal acquisition mechanisms to sample the incoming modulated signal. Use FPGA resources such as analog-to-digital converters (ADCs) to digitize the received analog signal.
Clock Recovery:

Implement clock recovery mechanisms to synchronize with the incoming signal. Techniques like Costas loop or Mueller and Muller clock recovery may be used, depending on the modulation scheme.
Digital Downconversion:

Perform digital downconversion to shift the signal from the carrier frequency to baseband. This involves multiplying the received signal by a local oscillator at the carrier frequency.
Filtering:

Apply filters to remove unwanted noise and interference. Filtering is crucial for improving the signal-to-noise ratio and facilitating accurate demodulation.
Demodulation Algorithm:

Implement the demodulation algorithm specific to the modulation scheme. For example:
In BPSK, compare the received signal with a reference to determine the transmitted bit.
In QPSK, use a phase-locked loop (PLL) and decision logic to decode the symbols.
In QAM, employ symbol detection techniques based on the constellation points.
Symbol Timing Recovery:

Implement symbol timing recovery to ensure accurate symbol synchronization. This is critical for correctly interpreting the received symbols.
Error Detection and Correction:

Integrate error detection and correction mechanisms to enhance the reliability of the demodulated data. Common techniques include Cyclic Redundancy Check (CRC) and Forward Error Correction (FEC).
Digital Signal Processing (DSP):

Utilize FPGA resources for digital signal processing tasks. FPGA-based DSP blocks can accelerate operations like filtering, correlation, and modulation/demodulation.
Parallel Processing and Pipelining:

Leverage parallel processing and pipelining techniques to enhance the efficiency of demodulation algorithms. FPGAs are well-suited for parallel processing tasks.
Memory Utilization:

Optimize the use of on-chip memory resources, such as block RAM, for storing and processing intermediate data. Efficient memory management can improve overall performance.
Implementation Language:

Use a Hardware Description Language (HDL) such as VHDL or Verilog to describe the demodulation algorithm and its hardware implementation.
Simulation and Verification:

Simulate the FPGA design using tools like ModelSim to verify the functionality and performance of the demodulation algorithm.
Integration with Communication System:

Integrate the FPGA-based demodulation module into the broader communication system. This involves interfacing with other components such as data sinks, channel decoding, and higher-level protocol layers.
FPGA Development Tools:

Utilize FPGA development tools provided by vendors to facilitate design, synthesis, and implementation. These tools often include IP cores and libraries for digital signal processing.
Demodulation in FPGA-based systems requires a thorough understanding of the specific modulation scheme and careful implementation of digital signal processing algorithms. Optimization techniques, parallel processing, and efficient memory management are crucial for achieving reliable and low-latency demodulation.


Image and Video Processing 
******************************************
FPGAs excel in video and image processing applications. They are used for tasks such as video compression/decompression, image recognition, and enhancement. FPGAs can be found in cameras, video processing equipment, and displays.

Image Processing 
******************************************
FPGA (Field-Programmable Gate Array) devices are well-suited for image processing applications due to their parallel processing capabilities, flexibility, and reconfigurability. Image processing on FPGA involves designing and implementing algorithms to manipulate and analyze digital images. Here are key considerations for FPGA-based image processing:

Hardware Description Language (HDL):

Use HDLs like VHDL or Verilog to describe the image processing algorithms and functionality in hardware. HDL allows you to design and program the FPGA at a low level.
Parallel Processing:

Leverage the parallel processing capabilities of FPGAs to perform image processing tasks in parallel. This can significantly improve processing speed and efficiency.
Image Input/Output Interfaces:

Implement interfaces to connect the FPGA with image sensors or other devices for image input and output. Common interfaces include Camera Serial Interface (CSI), Display Serial Interface (DSI), HDMI, or custom interfaces.
Image Pre-processing:

Perform preprocessing tasks such as color space conversion, resizing, filtering, and noise reduction. These tasks are essential for preparing the image for subsequent processing steps.
Image Filtering and Convolution:

Implement convolution operations for tasks like edge detection, blurring, and sharpening. These operations are fundamental in image processing and can be efficiently parallelized on FPGAs.
Feature Extraction:

Use FPGA to extract features from images, such as key points, edges, or texture features. Feature extraction is crucial for tasks like object recognition and tracking.
Image Compression/Decompression:

Implement image compression algorithms to reduce data size for storage or transmission. Common algorithms include JPEG or custom compression schemes.
Morphological Operations:

Implement morphological operations like dilation and erosion for shape analysis and manipulation.
Object Recognition and Tracking:

Develop algorithms for object recognition and tracking within images. This is commonly used in computer vision applications.
Real-Time Processing:

FPGAs are capable of real-time processing, making them suitable for applications that require low-latency image processing. Real-time capabilities are crucial in applications like video surveillance and robotics.
Memory Management:

Efficiently manage memory to store and retrieve image data. FPGA resources like block RAM can be utilized for on-chip storage.
Integration with External Components:

Integrate the FPGA with external components such as image sensors, displays, or communication interfaces. Ensure proper interfacing and synchronization between components.
FPGA Development Tools:

Utilize FPGA development tools provided by vendors (e.g., Vivado for Xilinx, Quartus for Intel) to facilitate design, synthesis, and implementation. These tools often include IP cores and libraries for image processing.
Simulation and Verification:

Simulate the image processing algorithms using tools like ModelSim to verify functionality before deploying to the FPGA.
Custom Hardware Accelerators:

Identify computationally intensive tasks and design custom hardware accelerators to offload these tasks from the CPU, improving overall system performance.
FPGA-based image processing provides a flexible and efficient platform for a wide range of applications, including computer vision, medical imaging, surveillance, and industrial automation.


Video Processing
******************************************
Implementing video processing in an FPGA (Field-Programmable Gate Array) allows for real-time and high-performance video processing tasks. Video processing in FPGAs is commonly used in applications such as image and video processing, computer vision, and multimedia systems. Here's an overview of the steps involved in implementing video processing in an FPGA:

Choose an FPGA with Sufficient Resources:

Select an FPGA that provides enough resources (logic elements, memory, DSP blocks) to handle the video processing tasks required for your application. Different FPGAs offer varying levels of resources and capabilities.
Understand Video Standards:

Familiarize yourself with video standards such as VGA, HDMI, or other video interfaces. Know the resolution, frame rate, and color space of the video signals you'll be working with.
Implement Video Input Interface:

Configure the FPGA to interface with the video source. This may involve implementing a video input interface for standards like VGA or HDMI. Use dedicated video input IP cores provided by FPGA vendors or create custom logic to handle video signal synchronization, decoding, and conversion.
Frame Buffer Storage:

Design a frame buffer to store video frames. Frame buffers are essential for processing video frames pixel by pixel. The size of the frame buffer depends on the resolution and color depth of the video.
Video Processing Algorithms:

Implement video processing algorithms based on your application requirements. Common video processing tasks include image enhancement, filtering, edge detection, color correction, and object recognition. Use hardware description languages (HDL) like Verilog or VHDL to describe the functionality.
Parallel Processing:

Leverage the parallel processing capabilities of FPGAs to perform pixel-level operations simultaneously. This is one of the strengths of FPGAs in video processing, as they can process multiple pixels or regions in parallel.
Video Output Interface:

Implement a video output interface to display or transmit the processed video. This may involve creating custom logic or using FPGA IP cores for video output standards such as VGA, HDMI, or others.
Timing Constraints:

Be mindful of timing constraints in video processing. Synchronize your design with the incoming video signals to ensure proper frame timing and pixel synchronization.
Hardware Acceleration:

Consider implementing hardware accelerators using DSP blocks or custom hardware for computationally intensive tasks. FPGAs provide flexibility in designing custom accelerators tailored to specific video processing algorithms.
Video Compression/Decompression:

Implement video compression or decompression if required. Standards like H.264 or JPEG can be implemented using FPGA resources to reduce bandwidth requirements for video transmission or storage.
Real-Time Processing:

Optimize your design for real-time processing if low-latency performance is crucial. FPGAs excel in real-time applications due to their parallel processing capabilities.
Testing and Debugging:

Use simulation tools and debugging features provided by FPGA development environments to test and validate your video processing design. Monitor signal waveforms, analyze timing diagrams, and verify the correctness of your implementation.
Integration with Software:

Integrate your FPGA-based video processing design with software running on a host system. This may involve developing drivers or application software to configure the FPGA and handle higher-level processing tasks.
Power Considerations:

Be aware of power consumption, especially if your application involves portable or embedded systems. Optimize your design for power efficiency where possible.
Compliance Testing:

Ensure that your video processing design complies with relevant video standards. Perform compliance testing to validate the interoperability of your FPGA-based video system with other devices.
When working on video processing in an FPGA, it's essential to refer to the documentation provided by the FPGA vendor, understand the specific requirements of the video standards you are working with, and thoroughly test your implementation to ensure its correctness and performance.



Wired/Wireless Communication
################################
FPGAs are utilized in wireless communication systems for tasks like baseband processing, modulation, and demodulation. They play a key role in software-defined radio (SDR) applications.


Symbol Mapping
******************************************
Symbol mapping in the context of digital communication refers to the process of associating symbols with specific bit sequences or values. This is a fundamental step in the modulation and demodulation process, where digital data is converted into a form suitable for transmission over a communication channel.

In FPGA-based systems, symbol mapping is often implemented using hardware description languages (HDL) such as VHDL or Verilog. The following steps outline a basic approach to symbol mapping in FPGA:

Define the Symbol Set:

Identify the set of symbols that will be used in the communication system. The symbol set depends on the modulation scheme being employed (e.g., BPSK, QPSK, QAM).
Map Bits to Symbols:

Assign specific bit patterns to each symbol in the symbol set. This mapping is typically predefined and agreed upon between the transmitter and receiver. For example, in BPSK, 0 might be mapped to one phase of the carrier signal, and 1 to the opposite phase.
Implement Symbol Mapping Logic:

In the FPGA design, implement logic that takes a stream of incoming bits and maps them to the corresponding symbols. This involves creating lookup tables or combinational logic to perform the mapping.

Consider Encoding Techniques:

Depending on the modulation scheme, additional encoding techniques may be applied before symbol mapping. For example, channel coding or scrambling may be employed to improve error resilience.
Simulation and Testing:

Simulate the symbol mapping logic using simulation tools like ModelSim to verify correct functionality. Ensure that the mapped symbols match the expected outcomes for different input bit sequences.
Integrate with Modulation Logic:

Integrate the symbol mapping logic with the modulation logic in the overall FPGA design. This may involve additional components for carrier generation, modulation schemes, and other aspects of the communication system.
Real-Time Considerations:

Consider real-time requirements and latency constraints. Optimize the symbol mapping logic for efficient and timely processing.
Symbol mapping is a critical component of the modulation process in digital communication systems. It establishes the relationship between digital data and the corresponding symbols used for transmission. Implementation details may vary based on the modulation scheme and specific requirements of the communication system.






Communications and Networking    
####################################
FPGAs are employed in networking equipment, including routers, switches, and network interface cards. They can be used to implement communication protocols, packet processing, and encryption/decryption tasks.

    Ethernet
::

    MAC - media access controller. This is the part of the system which converts a packet from the OS into a stream of bytes to be put on the wire (or fibre). Often interfaces to the host processor over something like PCI Express (for example).
    PHY - physical layer - converts a stream of bytes from the MAC into signals on one or more wires or fibres.
    MII - media independent interface. Just a standard set of pins between the MAC and the PHY, so that the MAC doesn't have to know or care what the physical medium is, and the PHY doesn't have to know or care how the host processor interface looks.
    The MII was standardised a long time ago and supports 100Mbit/sec speeds. A version using less pins is also available, RMII ('R' for reduced).

    For gigabit speeds, the GMII ('G' for gigabit) interface is used, with a reduced pincount version called RGMII. A very reduced pincount version called SGMII is also available ('S' for serial) which requires special capabilities on the IO pins of the MAC, whereas the other xMIIs are relatively conventional logic signals.    



    WIFI


Algorithm
##########################
    

Information Theory
##########################
Communication encoding refers to the process of converting information into a format suitable for transmission over a communication channel. Encoding is crucial in communication systems to ensure accurate and reliable data transfer. There are various encoding techniques used in different communication scenarios, each with its own advantages and applications. Here are a few common types:

Digital Modulation:

Binary Phase Shift Keying (BPSK): Represents binary data using two phases (0 and 180 degrees) of a carrier signal.
Quadrature Amplitude Modulation (QAM): Combines amplitude and phase modulation, allowing multiple bits to be transmitted in each symbol.
Line Coding:

Non-Return-to-Zero (NRZ): Uses two voltage levels to represent binary 0 and 1.
Manchester Encoding: Combines clock and data, ensuring a transition in the middle of each bit period.
4B/5B and 8B/10B Encoding: Used in high-speed data transmission to ensure a balance of 0s and 1s for clock recovery.
Error Detection and Correction:

Parity Bit: Adds an extra bit to the data to ensure an even or odd number of ones, detecting single-bit errors.
Cyclic Redundancy Check (CRC): Uses polynomial division to detect errors in transmitted data.
Analog Modulation:

Amplitude Modulation (AM): Varies the amplitude of a carrier signal to transmit analog information.
Frequency Modulation (FM): Varies the frequency of a carrier signal based on the input signal.
Spread Spectrum Techniques:

Direct Sequence Spread Spectrum (DSSS): Spreads the signal over a wide frequency band using a code.
Frequency Hopping Spread Spectrum (FHSS): Rapidly changes the carrier frequency during transmission.
Run-Length Encoding (RLE):

Used in Data Compression: Represents repeated consecutive data with a count value.
These encoding techniques are selected based on factors like data rate, bandwidth, noise resistance, and power consumption, among others. The choice of encoding plays a significant role in the overall performance and reliability of a communication system.





Encoding
******************************************
Decoding
******************************************


|   BCH Encoder
|   LDPC Encoder
|   CRC
    Error Detection and correction

    
Data Structure
##########################


Controls
##########################





Organize...
##########################

|   LFSR
|   Pseudo random binary sequence

