/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const getCryptoPrice = /* GraphQL */ `
  query GetCryptoPrice($id: ID!) {
    getCryptoPrice(id: $id) {
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
export const listCryptoPrices = /* GraphQL */ `
  query ListCryptoPrices(
    $filter: ModelCryptoPriceFilterInput
    $limit: Int
    $nextToken: String
  ) {
    listCryptoPrices(filter: $filter, limit: $limit, nextToken: $nextToken) {
      items {
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
      nextToken
      startedAt
      __typename
    }
  }
`;
export const syncCryptoPrices = /* GraphQL */ `
  query SyncCryptoPrices(
    $filter: ModelCryptoPriceFilterInput
    $limit: Int
    $nextToken: String
    $lastSync: AWSTimestamp
  ) {
    syncCryptoPrices(
      filter: $filter
      limit: $limit
      nextToken: $nextToken
      lastSync: $lastSync
    ) {
      items {
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
      nextToken
      startedAt
      __typename
    }
  }
`;
