package org.firstinspires.ftc.teamcode.OldCode;

import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import org.firstinspires.ftc.robotcore.external.tfod.Recognition;
import org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName;
import org.firstinspires.ftc.robotcore.external.ClassFactory;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.util.ElapsedTime;
import com.qualcomm.robotcore.util.Range;



// import org.firstinspires.ftc.robotcore.external.ClassFactory;
// import org.firstinspires.ftc.robotcore.external.navigation.VuforiaLocalizer;
// import org.firstinspires.ftc.robotcore.external.navigation.VuforiaLocalizer.CameraDirection;
// import org.firstinspires.ftc.robotcore.external.tfod.Recognition;
// import org.firstinspires.ftc.robotcore.external.tfod.TFObjectDetector;

import java.util.List;

@Autonomous(name = "BlueLeft", group = "BlueLeft")
public class BlueLeft extends LinearOpMode {
    private DcMotor FrontRight; // defines variables to be used in the code
    private DcMotor FrontLeft;
    private DcMotor BackRight;
    private DcMotor BackLeft;
    private DcMotor RightShooter; // this is where we define the variables
    private DcMotor LeftShooter;
    private DcMotor RightLoader;
    private DcMotor LeftLoader;
    private Servo LeftWobble;
    private Servo RightWobble;
    


    @Override
    public void runOpMode() {

        telemetry.addData("Status", "Initialized");
        telemetry.update();
        
        FrontRight = (DcMotor) hardwareMap.get("FrontRight"); // this is where we assign variables to parts
        FrontLeft = (DcMotor) hardwareMap.get("FrontLeft");
        BackRight = (DcMotor) hardwareMap.get("BackRight");
        BackLeft = (DcMotor) hardwareMap.get("BackLeft");
        RightShooter = (DcMotor) hardwareMap.get("RightShooter"); // this is where we assign parts to variables
        LeftShooter = (DcMotor) hardwareMap.get("LeftShooter");
        LeftLoader = (DcMotor) hardwareMap.get("LeftLoader");
        RightLoader = (DcMotor) hardwareMap.get("RightLoader");
        LeftWobble = (Servo) hardwareMap.get("LeftWobble");
        RightWobble = (Servo) hardwareMap.get("RightWobble");
        // RotateServo = (Servo) hardwareMap.get("RotateServo");

        FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        

        FrontLeft.setDirection(DcMotor.Direction.REVERSE);
        BackLeft.setDirection(DcMotor.Direction.REVERSE);
        
        

        waitForStart();
        

                                    RightWobble.setPosition(.76);
                                    LeftWobble.setPosition(.14);
                                    sleep(500);
                                    
                                    

        
                                    // FrontLeft.setTargetPosition(1920);//drive forward to the A zone
                                    // FrontLeft.setPower(0.84);
                                    // FrontRight.setPower(0.74);
                                    // BackLeft.setPower(0.84);
                                    // BackRight.setPower(0.74);
                                    // // LeftShooter.setPower(-0.63);
                                    // // RightShooter.setPower(0.63);
                                    
                                    
                                    // while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    // }
                                    // FrontRight.setPower(0);
                                    // FrontLeft.setPower(0);
                                    // BackLeft.setPower(0);
                                    // BackRight.setPower(0);
                                    // sleep(2000);
                                    
                                    // //
                                    
                                    // FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    // sleep(50);
                                    // FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    // FrontLeft.setTargetPosition(-155);//drive backwards slightly for room to turn
                                    // FrontLeft.setPower(-0.5);
                                    // FrontRight.setPower(-0.45);
                                    // BackLeft.setPower(-0.5);
                                    // BackRight.setPower(-0.5);
                                    // // LeftShooter.setPower(-0.63);
                                    // // RightShooter.setPower(0.63);
                                    // // LeftLoader.setPower(-1);
                                    // // RightLoader.setPower(1);
                                    
                                    
                                    // while (FrontLeft.getCurrentPosition() > FrontLeft.getTargetPosition()){
                                        
                                    // }
                                    // FrontRight.setPower(0);
                                    // FrontLeft.setPower(0);
                                    // BackLeft.setPower(0);
                                    // BackRight.setPower(0);
                                    // LeftShooter.setPower(0);
                                    // RightShooter.setPower(0);
                                    // LeftLoader.setPower(0);
                                    // RightLoader.setPower(0);
                                    // sleep(2000);
                                    
                                    // //
                                    
                                    // FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    // sleep(50);
                                    // FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    // FrontLeft.setTargetPosition(980);//turn 90 degrees to the left
                                    // FrontLeft.setPower(0.5);
                                    // FrontRight.setPower(-0.45);
                                    // BackLeft.setPower(0.5);
                                    // BackRight.setPower(-0.5);
                                    
                                    
                                    // while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    // }
                                    // FrontRight.setPower(0);
                                    // FrontLeft.setPower(0);
                                    // BackLeft.setPower(0);
                                    // BackRight.setPower(0);
                                    // sleep(2000);
                                    
                                    // //
                                    
                                    // FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    // sleep(50);
                                    // FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    // FrontLeft.setTargetPosition(1200);//drive forward slightly in front of power pegs
                                    // FrontLeft.setPower(0.54);
                                    // FrontRight.setPower(0.44);
                                    // BackLeft.setPower(0.54);
                                    // BackRight.setPower(0.44);
                                    
                                    
                                    // while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    // }
                                    // FrontRight.setPower(0);
                                    // FrontLeft.setPower(0);
                                    // BackLeft.setPower(0);
                                    // BackRight.setPower(0);
                                    // sleep(2000);
                                    
                                    // //
                                    
                                    // FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    // sleep(50);
                                    // FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    // FrontLeft.setTargetPosition(-585);//turn left 90 degrees to aim at the power pegs
                                    // FrontLeft.setPower(-0.5);
                                    // FrontRight.setPower(0.45);
                                    // BackLeft.setPower(-0.5);
                                    // BackRight.setPower(0.5);
                                    // LeftShooter.setPower(-0.6);
                                    // RightShooter.setPower(0.6);
                                    
                                    
                                    // while (FrontLeft.getCurrentPosition() > FrontLeft.getTargetPosition()){
                                        
                                    // }
                                    // FrontRight.setPower(0);
                                    // FrontLeft.setPower(0);
                                    // BackLeft.setPower(0);
                                    // BackRight.setPower(0);
                                    // sleep(1000);
                                    
                                    
                                    // LeftShooter.setPower(-0.60);
                                    // RightShooter.setPower(0.60);
                                    // LeftLoader.setPower(-1);
                                    // RightLoader.setPower(1);
                                    // sleep(5000);
                                    
                                    // LeftShooter.setPower(0);
                                    // RightShooter.setPower(0);
                                    // LeftLoader.setPower(0);
                                    // RightLoader.setPower(0);
                                    
                                    // FrontLeft.setPower(0.8);
                                    // FrontRight.setPower(0.8);
                                    // BackLeft.setPower(0.8);
                                    // BackRight.setPower(0.8);
                                    // sleep(170);
                                    
                                    
                                    // FrontRight.setPower(0);
                                    // FrontLeft.setPower(0);
                                    // BackLeft.setPower(0);
                                    // BackRight.setPower(0);
                                    
                                    //B
                                    
                                    FrontLeft.setTargetPosition(2900);//drive forward to the B zone
                                    FrontLeft.setPower(0.84);
                                    FrontRight.setPower(0.7);
                                    BackLeft.setPower(0.84);
                                    BackRight.setPower(0.7);
                                    // LeftShooter.setPower(-0.63);
                                    // RightShooter.setPower(0.63);
                                    
                                    
                                    while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    }
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
                                    sleep(2000);
                                    
                                    //
                                    
                                    FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    sleep(50);
                                    FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    FrontLeft.setTargetPosition(-155);//drive backwards slightly for room to turn
                                    FrontLeft.setPower(-0.5);
                                    FrontRight.setPower(-0.45);
                                    BackLeft.setPower(-0.5);
                                    BackRight.setPower(-0.5);
                                    // LeftShooter.setPower(-0.63);
                                    // RightShooter.setPower(0.63);
                                    // LeftLoader.setPower(-1);
                                    // RightLoader.setPower(1);
                                    
                                    
                                    while (FrontLeft.getCurrentPosition() > FrontLeft.getTargetPosition()){
                                        
                                    }
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
                                    LeftShooter.setPower(0);
                                    RightShooter.setPower(0);
                                    LeftLoader.setPower(0);
                                    RightLoader.setPower(0);
                                    sleep(2000);
                                    
                                    //
                                    
                                    FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    sleep(50);
                                    FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    FrontLeft.setTargetPosition(835);//turn 90 degrees to the left
                                    FrontLeft.setPower(0.5);
                                    FrontRight.setPower(-0.45);
                                    BackLeft.setPower(0.5);
                                    BackRight.setPower(-0.5);
                                    
                                    
                                    while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    }
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
                                    sleep(2000);
                                    
                                    //
                                    
                                    FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    sleep(50);
                                    FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    FrontLeft.setTargetPosition(1050);//drive forward slightly in front of power pegs
                                    FrontLeft.setPower(0.54);
                                    FrontRight.setPower(0.44);
                                    BackLeft.setPower(0.54);
                                    BackRight.setPower(0.44);
                                    
                                    
                                    while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    }
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
                                    sleep(2000);
                                    
                                    //
                                    
                                    FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    sleep(50);
                                    FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    FrontLeft.setTargetPosition(865);//turn right 90 degrees
                                    FrontLeft.setPower(0.5);
                                    FrontRight.setPower(-0.45);
                                    BackLeft.setPower(0.5);
                                    BackRight.setPower(-0.5);
                                    // LeftShooter.setPower(-0.6);
                                    // RightShooter.setPower(0.6);
                                    
                                    
                                    while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    }
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
                                    sleep(1000);
                                    
                                    FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    sleep(50);
                                    FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    FrontLeft.setTargetPosition(725);//drive forward past launch line
                                    FrontLeft.setPower(0.54);
                                    FrontRight.setPower(0.44);
                                    BackLeft.setPower(0.54);
                                    BackRight.setPower(0.44);
                                    
                                    
                                    while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    }
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
                                    sleep(2000);
                                    
                                    FrontLeft.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                                    sleep(50);
                                    FrontLeft.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                                    FrontLeft.setTargetPosition(2200);//turn left 180 degrees to aim at the power pegs
                                    FrontLeft.setPower(0.5);
                                    FrontRight.setPower(-0.45);
                                    BackLeft.setPower(0.5);
                                    BackRight.setPower(-0.5);
                                    LeftShooter.setPower(-0.6);
                                    RightShooter.setPower(0.6);
                                    
                                    
                                    while (FrontLeft.getCurrentPosition() < FrontLeft.getTargetPosition()){
                                        
                                    }
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
                                    sleep(1000);
                                    
                                    
                                    LeftShooter.setPower(-0.60);
                                    RightShooter.setPower(0.60);
                                    LeftLoader.setPower(-1);
                                    RightLoader.setPower(1);
                                    sleep(5000);
                                    
                                    LeftShooter.setPower(0);
                                    RightShooter.setPower(0);
                                    LeftLoader.setPower(0);
                                    RightLoader.setPower(0);
                                    
                                    FrontLeft.setPower(0.8);
                                    FrontRight.setPower(0.8);
                                    BackLeft.setPower(0.8);
                                    BackRight.setPower(0.8);
                                    sleep(170);
                                    
                                    
                                    FrontRight.setPower(0);
                                    FrontLeft.setPower(0);
                                    BackLeft.setPower(0);
                                    BackRight.setPower(0);
        
        
    }
}
