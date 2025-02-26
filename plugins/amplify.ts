import { defineNuxtPlugin } from "#app";
import { Amplify} from "aws-amplify";

export default defineNuxtPlugin((nuxtApp) => {
    Amplify.configure({
        Auth: {
          Cognito: {
            userPoolId: "ap-northeast-1_N0bIGCilQ",
            userPoolClientId: "5uvlhqe5n6rmnn8hv299h63nm2",
            identityPoolId: "",
            loginWith: {
              email: true,
            },
            signUpVerificationMethod: "code",
            userAttributes: {
              email: {
                required: true,
              },
            },
            allowGuestAccess: true,
            passwordFormat: {
              minLength: 8,
              requireLowercase: true,
              requireUppercase: true,
              requireNumbers: true,
              requireSpecialCharacters: true,
            },
          },
        },
      })
});