## FFMPEG Example Commands

#### 1. Converting Files

	#Using default settings w/ default codec library
	ffmpeg -i /path/to/input /path/to/output

	#Specifying a codec library
	ffmpeg -i /path/to/input -c:v libx264 /path/to/output

	#Average bit rate
	ffmpeg -i /path/to/input -c:v libx264 -b:v 100k -bufsize 50k /path/to/output #bufsize tells the encoder how often to calculate average bitrate

	#Setting Min and Max bitrate
	ffmpeg -i /path/to/input -c:v libx264 -b:v 100k -bufsize 50k -minrate 50k -maxrate 50k /path/to/output

	#Using constant rate factor (visually lossless)
	ffmpeg -i /path/to/input -c:v libx264 -crf 18 /path/to/output

	#Restricting the output file size
	Bitrate = output file size in MB * 8192 (convert MB to KB) / Duration in seconds

	From there, two-pass, variable bit rate (VBR) compression can be used to yield an approximate file size:

	ffmpeg -i input -c:v libx264 -preset slow -b:v (calculated bitrate) -strict -2
	-pass 1 -f mp4 /dev/null && ffmpeg -i input -c:v libx264 -preset slow -b:v (calculated bitrate) –strict -2 -pass 2 output.mp4

#### 2. Transcoding Files for Streaming

	#Creating a webm file
	ffmpeg -i /path/to/input -c:v libvpx -crf 23 -b:v 1M -c:a libvorbis /path/to/output.webm #where -b:v is the max bitrate

	#Creating an H.264 file
	ffmpeg -i /path/to/input -c:v libx264 -crf 23 -strict -2 -pix_fmt yuv420p -movflags faststart /path/to/output.mp4

#### 3. Stream Mapping

	#Copy video stream and transcode audio stream
	ffmpeg -i /path/to/input -c:v copy -map 0:1 -c:a aac -strict -2 /path/to/output.mp4

	#Remove audio
	ffmpeg -i /path/to/input -c:v copy -map 0:1 -an -strict -2 /path/to/output.mp4 #audio null

	#Export audio and video to separate files
	ffmpeg -i /path/to/input -map 0:0 /path/to/output.mp4 -map 0:1 /path/to/output.wav #defaults to 16 bit pcm

#### 4. Time-Based Commands

	#Export sections of a video
	ffmpeg -i /path/to/input -ss 00:00:00 -to 00:00:30 -c:v libx264 /path/to/output #export first 30 seconds of a video

	#Export a single frame as an image
	ffmpeg -i input.flv -ss 00:00:14.435 -vframes 1 out.png

	#Export to a dpx sequence
	ffmpeg -i input -r 24 -an -pix_fmt rgb24 /output/frames/frame_%06d.dpx

	#Animate an image sequence
	ffmpeg -i frames/frame_%06d.dpx -r 24 -vcodec prores -profile:v 2 out.mov #0 : ProRes422 (Proxy) 1 : ProRes422 (LT) 2 : ProRes422 (Normal) 3 : ProRes422 (HQ)

#### 5. Image Manipulation

	#Scale
	ffmpeg -i /path/to/input -c:v libx264 -vf scale=1920:1080 /path/to/output.mp4 #w:h

	#Crop
	

#### 6. Batch Processing

	#Batch process files
	for x in *.avi; do
		ffmpeg -i $x -c:v libx264 -strict -2 ${x%.avi}.mp4;
	done
