/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const createCryptoPrice = /* GraphQL */ `
  mutation CreateCryptoPrice(
    $input: CreateCryptoPriceInput!
    $condition: ModelCryptoPriceConditionInput
  ) {
    createCryptoPrice(input: $input, condition: $condition) {
      id
      Date
      Coin
      Price
      createdAt
      updatedAt
      _version
      _deleted
      _lastChangedAt
      __typename
    }
  }
`;
export const updateCryptoPrice = /* GraphQL */ `
  mutation UpdateCryptoPrice(
    $input: UpdateCryptoPriceInput!
    $condition: ModelCryptoPriceConditionInput
  ) {
    updateCryptoPrice(input: $input, condition: $condition) {
      id
      Date
      Coin
      Price
      createdAt
      updatedAt
      _version
      _deleted
      _lastChangedAt
      __typename
    }
  }
`;
export const deleteCryptoPrice = /* GraphQL */ `
  mutation DeleteCryptoPrice(
    $input: DeleteCryptoPriceInput!
    $condition: ModelCryptoPriceConditionInput
  ) {
    deleteCryptoPrice(input: $input, condition: $condition) {
      id
      Date
      Coin
      Price
      createdAt
      updatedAt
      _version
      _deleted
      _lastChangedAt
      __typename
    }
  }
`;
