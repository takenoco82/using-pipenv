pipeline {
  agent any
  stages {
    stage('write file') {
      steps {
        writeFile(file: "output.txt", text: "${OUTPUT_TEXT}")
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
