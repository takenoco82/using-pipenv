pipeline {
  agent any
  environment {
    file_name = "output.txt"
  }
  stages {
    stage('parallel build') {
      steps {
        parallel(
          "01_hello_world": {
            echo '01_hello_world'
          },
          "02_use_sh_step": {
            sh 'echo 02_use_sh_step'
          },
          "03_write_file": {
            writeFile(file: file_name, text: "output_text")
          }
        )
      }
    }
  }
  post {
    always {
      // Always cleanup after the build.
      sh 'echo finished!'
    }
  }
}
